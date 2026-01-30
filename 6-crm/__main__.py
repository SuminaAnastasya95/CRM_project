"""Точка входа"""

from orders import create_order, list_orders


def start_menu():
    print("Что вы хотите сделать?\n"
          "Создать заказ? Команда -> create\n"
          "Показать лист заказов? Команда -> list\n"
          "Изменить заказ? Команда -> edit\n"
          "Удалить заказ? Команда -> delete\n"
          "Выход? Команда -> exit")
    while True:
        menu = input(">>> ").strip()
        match menu:
            case "create":
                create_order()
            case "list":
                list_orders()
            # case 'edit':
                # edit_order()
        #     continue
        # if menu == 'delete':
        #     remove_order()
        #     continue
            case 'exit':
                print("Завершение программы...")
                exit()
            case _:
                print("Не знаю такой команды")


if __name__ == "__main__":
    start_menu()
