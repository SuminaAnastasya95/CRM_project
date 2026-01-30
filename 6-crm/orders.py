"""Бизнес-логика заказов"""
from datetime import datetime, date
from cli import parss_create_order
from utils.validators import make_order


scroll_orders = {}


def create_order():
    """Создание заказа"""
    order = input("Что было заказано?\n>>> ")
    item_order = [item.strip() for item in order.split(',')]
    title, amount, email_val, status, tags, due = parss_create_order(
        item_order)
    new_id = len(scroll_orders) + 1
    new_order = make_order(
        id_=new_id,
        title=title,
        amount=amount,
        email=email_val,
        status=status,
        tags=tags,
        due=due,
        created_at=None,  # make_order сам подставит текущую дату
        closed_at=None
    )
    scroll_orders[new_id] = new_order

    print(f"Заказ #{new_id} успешно добавлен!")
    return new_order


def list_orders():
    return print("Перечень заказов: ", scroll_orders)


def edit_order():
    """Изменения заказа"""
    print("Перечень заказов", scroll_orders)
    try:
        choice_order = input("Какой заказ хотите изменить?\n"
                             ">>> ")
        change = input("Какой параметр хотите изменить?\n"
                       "< title > amount= 123,22 email= <email> status=['new', 'in_progress', 'done', 'cancelled'] [tags=a, b, c] [due=YYYY-MM-DD]\n"
                       ">>> ")
        match change:
            case "title":
                pass
    except ValueError as e:
        print(f"Передан не валидный параметр - {e}")


def remove_order():
    """Удаление заказа"""
    pass


# if __name__ == "__main__":
#     create_order()
