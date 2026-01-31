"""Бизнес-логика заказов"""
from datetime import datetime, date
from cli import parss_create_order
from utils.validators import make_order, make_edit


orders_dict = {}


def create_order():
    """Создание заказа"""
    order = input("Что было заказано?\n>>> ")
    item_order = [item.strip() for item in order.split(',')]
    title, amount, email_val, status, tags, due = parss_create_order(
        item_order)
    new_id = len(orders_dict) + 1
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
    orders_dict[new_id] = new_order
    print(f"Заказ #{new_id} успешно добавлен!")
    return new_order


def get_all_orders():
    return orders_dict


def list_orders():
    orders = get_all_orders()
    if not orders:
        print("Список пуст")
        return
    for o_id, data in orders_dict.items():
        print(
            f"Номер заказа - {o_id}, Название - {data["title"]}, Статус - {data["status"]}")


def edit_order():
    """Изменения заказа"""
    print("---Перечень заказов---")
    for o_id, data in orders_dict.items():
        print(
            f"Номер заказа - {o_id}, Название - {data["title"]}, Статус - {data["status"]}")
    try:
        choice_order = int(input("Введите номер заказа, который хотите изменить?\n"
                                 ">>> "))
        if choice_order not in orders_dict:
            print("❌Данный номер заказа отсутствует")
            return
        change = input("Какой параметр хотите изменить?\n"
                       "title, amount, email, status, tags\n"
                       ">>> ")
        if change not in orders_dict[choice_order]:
            print(f"Параметр {change} отсутствует в списке")
            return
        make_edit(orders_dict, choice_order, change)
        return
    except ValueError as e:
        print(f"Ошибка ввода - {e}")


def remove_order():
    """Удаление заказа"""
    try:
        order_id = int(input("Введите номер заказа, который хотите удалить?\n"
                             ">>> "))
        if order_id not in orders_dict:
            print("❌Данный номер заказа отсутствует")
            return
        del orders_dict[order_id]
        print(f"Заказ #{order_id} успешно удален.")
    except ValueError:
        print("Ошибка данных")


# if __name__ == "__main__":
#     edit_order()
