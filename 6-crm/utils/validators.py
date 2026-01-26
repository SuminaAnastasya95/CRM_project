from datetime import datetime
from typing import TypedDict

STATUS = ['new', 'in_progress', 'done', 'cancelled']


class Order(TypedDict):
    id: int  # уникальный идентификатор (int).
    title: str  # название заказа (строка).
    amount: float  # сумма заказа (число с плавающей точкой).
    email: str  # email клиента (строка).
    status: str  # статус заказа (new, in_progress, done, cancelled).
    tags: set[str]  # множество тегов (set строк).
    created_at: datetime  # дата и время создания (ISO 8601, UTC).
    due:  datetime  # дедлайн (строка в ISO 8601 или None).
    # дата и время закрытия заказа (ISO 8601, UTC или None).
    closed_at: datetime
