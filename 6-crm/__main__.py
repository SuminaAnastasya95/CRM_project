"""Точка входа"""

from orders import create_order, list_orders, edit_order, remove_order


def start_menu():
    print("""
Что вы хотите сделать?
Создать заказ?         Команда -> create
Показать лист заказов? Команда -> list
Изменить заказ?        Команда -> edit
Удалить заказ?         Команда -> delete
Выход?                 Команда -> exit
    """)
    while True:
        menu = input(">>> ").strip()
        match menu:
            case "create":
                create_order()
            case "list":
                list_orders()
            case 'edit':
                edit_order()
            case 'delete':
                remove_order()

            case 'exit':
                print("Завершение программы...")
                exit()
            case _:
                print("Не знаю такой команды")


if __name__ == "__main__":
    start_menu()
