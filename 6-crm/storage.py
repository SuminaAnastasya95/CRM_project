"""Работа с JSON"""
import json
from utils.validators import Order
from cli import pars_date


def load(path: str):  # 1. Добавлен путь
    raw = {}
    try:
        with open(path, "r", encoding='utf-8') as f:
            raw = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return [], 1

    orders_list: list[Order] = []
    max_id = 0

    for item in raw.get('orders', []):
        try:
            order_item: Order = {
                "id": int(item["id"]),
                "title": item["title"],
                "amount": float(item.get("amount", 0)),
                "email": item.get("email", ""),
                "status": item["status"],
                "tags": list(item.get("tags", [])),
                'created_at': item.get("created_at"),
                'due': item.get("due"),
                'closed_at': item.get("closed_at")
            }
            orders_list.append(order_item)
            max_id = max(max_id, order_item["id"])
        except Exception as e:
            print(f"[WARN] - пропущена запись: {e}")

    return orders_list, max_id + 1


def save(path, orders):
    data = {
        'orders': [{  # Используем множественное число для ключа
            'id': o['id'],
            'title': o['title'],
            'amount': o['amount'],
            'email': o['email'],
            'status': o['status'],
            'tags': o['tags'],
            # 2. Просто берем строку, JSON не примет объект date
            'due': o.get('due'),
            # 3. Добавляем недостающие поля для персистентности
            'created_at': o.get('created_at'),
            'closed_at': o.get('closed_at')
        } for o in orders]
    }
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
