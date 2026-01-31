"""Проверка id/ полей"""

from datetime import datetime, date, timezone
from typing import TypedDict, Optional
from cli import pars_date

STATUS = ['new', 'in_progress', 'done', 'cancelled']


class Order(TypedDict):
    id: int  # уникальный идентификатор (int).
    title: str  # название заказа (строка).
    amount: float  # сумма заказа (число с плавающей точкой).
    email: str  # email клиента (строка).
    status: str  # статус заказа (new, in_progress, done, cancelled).
    tags: Optional[set[str]]  # множество тегов (set строк).
    created_at: Optional[str]  # дата и время создания (ISO 8601, UTC).
    due:  Optional[str]  # дедлайн (строка в ISO 8601 или None).
    # дата и время закрытия заказа (ISO 8601, UTC или None).
    closed_at: Optional[str]


def make_order(id_: int, title: str, amount: float, email: str, due:  datetime, closed_at:  Optional[datetime] = None,  created_at: Optional[datetime] = None,  status: str = "new", tags: Optional[set[str]] = None) -> Order:
    if status not in STATUS:
        raise ValueError(
            "Не правильный статус. Возможны только 'new', 'in_progress', 'done', 'cancelled'")
    if created_at is None:
        created_at = datetime.now(timezone.utc)
    order: Order = {
        "id": id_,
        "title": title.strip(),
        "amount": amount,
        "email": email,
        "status": status,
        "tags": tags,
        "created_at": created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "due": due.strftime("%Y-%m-%d") if due else None,
        'closed_at':  closed_at.strftime("%Y-%m-%d %H:%M:%S") if closed_at else None
    }
    return order


def make_edit(orders_dict: dict, choice_order: int, change: str):
    order = orders_dict[choice_order]
    new_val = str(
        input("На какое значение, хотите изменить?>>> "))
    match change:
        case "title" | "email" | "status":
            order[change] = new_val
            print(order[change])
        case "amount":
            try:
                order["amount"] = float(new_val.replace(",", '.'))
            except ValueError as e:
                print("Значение должно быть числом")
        case "tags":
            new_tags = {t.strip() for t in new_val.split(",")}
            kind = input("Изменить/ добавить?>>> ").lower()
            if kind == "изменить" and order["tags"]:
                order["tags"].update(new_tags)
            else:
                order["tags"] = new_tags
        case "due":
            try:
                order["due"] = pars_date(new_val).strftime("%Y-%m-%d")
            except ValueError:
                print("Не верный формат даты")
    print(f"✅ Обновленный заказ: {order}")


# if __name__ == "__main__":
#     make_edit()
