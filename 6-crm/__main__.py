"""Точка входа"""

from orders import create_order, list_orders, edit_order, remove_order
from storage import load, save
from utils.validators import Order


def start_menu():
    print("""
Что вы хотите сделать?
Создать заказ?         Команда -> create
Показать лист заказов? Команда -> list
Изменить заказ?        Команда -> edit
Удалить заказ?         Команда -> delete
Выход?                 Команда -> exit
    """)
    orders: list[Order] = []
    next_id = 1
    file_orders = 'order.json'
    orders, next_id = load(file_orders)
    file_path = 'order.json'
    try:
        while True:
            menu = input(">>> ").strip()
            match menu:
                case "create":
                    new_order, next_id = create_order(next_id)
                    orders.append(new_order)
                case "list":
                    list_orders()
                case 'edit':
                    edit_order()
                case 'delete':
                    remove_order()

                case 'exit':
                    save(file_path, orders)
                    print("Завершение программы...")
                    exit()
                case _:
                    print("Не знаю такой команды")
    except KeyboardInterrupt:
        save(file_path, orders)
    except Exception as e:
        save(file_path, orders)
        print("[ERROR] - ", e)


if __name__ == "__main__":
    start_menu()
