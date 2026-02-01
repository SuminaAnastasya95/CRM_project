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
        # Это норма при первом запуске, сообщение не нужно
        return [], 1
    except json.JSONDecodeError:
        # ТРЕБОВАНИЕ: вывод понятного сообщения при повреждении
        print(
            f"⚠️ Ошибка: файл {path} поврежден или содержит некорректный JSON. Начинаем с чистого листа.")
        return [], 1

    orders_list: list[Order] = []
    max_id = 0

    # РЕШЕНИЕ: Ключ синхронизирован ('orders'), теперь данные подгрузятся
    for item in raw.get('orders', []):
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
            print(f"[WARN] - Пропущена некорректная запись в JSON: {e}")

    return orders_list, max_id + 1


def save(path, orders):
    data = {
        # РЕШЕНИЕ: ключ 'orders' во множественном числе, как в методе load
        'orders': [{
            'id': o['id'],
            'title': o['title'],
            'amount': o['amount'],
            'email': o['email'],
            'status': o['status'],
            'tags': o['tags'],
            'due': o.get('due'),
            'created_at': o.get('created_at'),
            'closed_at': o.get('closed_at')
        } for o in orders]
    }
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
