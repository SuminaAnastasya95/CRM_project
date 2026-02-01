"""Работа с JSON"""
import json
from utils.validators import Order
from cli import pars_date


def load(path: str):  # 1. Добавлен путь
    raw = {}
    try:
        with open(path, "r", encoding='utf-8') as f:
            raw = json.load(f)
    except FileNotFoundError:
        return [], 1
    except json.JSONDecodeError as e:
        print(f'[WARN] - Поврежденный JSON ({path}) : {e}')
        return [], 1  # Важно вернуть значения, если файл битый

    order: list[Order] = []
    max_id = 0

    for item in raw.get('order', []):
        try:
            order: Order = {
                "id": int(item["id"]),
                "title": item["title"],
                "amount": float(item.get("amount", 0)),  # .get безопаснее
                "email": item.get("email", ""),
                "status": item["status"],
                "tags": list(item.get("tags", [])),  # 2. Исправлено здесь
                'created_at': pars_date(item.get("due")) if item.get("due") else None,
                'due': str(item['due']) if item.get("due") else None,
                'closed_at': pars_date(item.get("closed_at")) if item.get("closed_at") else None
            }
            order.append(order)
            max_id = max(max_id, order["id"])
        except Exception as e:
            print(f"[WARN] - пропущена задача: {e}")

    return order, max_id + 1


def save(path, order):  # Добавили аргументы
    data = {
        'order': [{
            'id': t['id'],
            'title': t['title'],
            'amount': t['amount'],
            'email': t['email'],
            'status': t['status'],
            'tags': t['tags'],
            # Здесь используем формат (в строку), а не парс
            'due': pars_date(t['due']) if t.get("due") else None
        }
            for t in order
        ]
    }
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
