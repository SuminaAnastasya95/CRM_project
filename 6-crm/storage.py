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
        # Это штатная ситуация, сообщение не требуется
        return [], 1
    except json.JSONDecodeError as e:
        # Выполняем требование по понятному сообщению
        print(
            f"⚠️ Файл {path} поврежден или имеет неверный формат: {e}. Начинаем с пустого списка.")
        return [], 1

    orders_list: list[Order] = []
    max_id = 0

    # Исправлено: теперь ключ 'orders' совпадает в load и save
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
        except (KeyError, TypeError, ValueError) as e:
            print(f"[WARN] - Пропущена запись из-за ошибки в данных: {e}")

    return orders_list, max_id + 1


def save(path, orders):
    data = {
        'orders': [{  # Ключ синхронизирован с методом load
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
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[ERROR] - Не удалось сохранить файл: {e}")
