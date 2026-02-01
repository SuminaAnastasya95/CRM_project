"""Работа с JSON"""
import json
from utils.validators import Order
from cli import pars_date


def load(path: str):
    raw = {}
    try:
        with open(path, "r", encoding='utf-8') as f:
            raw = json.load(f)
    except FileNotFoundError:
        return [], 1
    except json.JSONDecodeError:
        # ИСПРАВЛЕНО: Теперь выводится понятное сообщение согласно требованию
        print(
            f"⚠️ Ошибка: файл {path} поврежден или содержит некорректный JSON. Загружен пустой список.")
        return [], 1

    orders_list: list[Order] = []
    max_id = 0

    # ИСПРАВЛЕНО: Используем ключ 'orders' (соответствует функции save)
    for item in raw.get('order', []):
        try:
            order_item: Order = {
                "id": int(item["id"]),
                "title": item["title"],
                "amount": float(item.get("amount", 0)),
                "email": item.get("email", ""),
                "status": item["status"],
                "tags": list(item.get("tags", [])),
                "created_at": item.get("created_at"),
                "due": item.get("due"),
                "closed_at": item.get("closed_at")
            }
            orders_list.append(order_item)
            max_id = max(max_id, order_item["id"])
        except (KeyError, ValueError, TypeError) as e:
            print(f"[WARN] - Пропущена некорректная запись в файле: {e}")

    return orders_list, max_id + 1


def save(path, order):
    # ИСПРАВЛЕНО: Ключ 'orders' теперь един для записи и чтения
    data = {
        'order': [{
            'id': o['id'],
            'title': o['title'],
            'amount': o['amount'],
            'email': o['email'],
            'status': o['status'],
            'tags': o['tags'],
            'due': o.get('due'),
            'created_at': o.get('created_at'),
            'closed_at': o.get('closed_at')
        } for o in order]
    }
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
