"""Точка входа"""

from orders import create_order, list_orders, edit_order, remove_order
from storage import load, save
from utils.validators import Order


def start_menu():
    print("""
==== CRM Система ====
Доступные команды:
create - Создать заказ
list   - Показать все заказы
edit   - Изменить заказ
delete - Удалить заказ
exit   - Сохранить и выйти
    """)

    file_path = 'order.json'
    # 1. Загружаем данные при старте
    orders, next_id = load(file_path)

    try:
        while True:
            menu = input("\n>>> ").strip().lower()

            match menu:
                case "create":
                    # Получаем новый заказ и обновленный счетчик ID
                    new_order, next_id = create_order(next_id)
                    orders.append(new_order)
                    print(f"✅ Заказ №{new_order['id']} добавлен в список.")

                case "list":
                    # Передаем текущие заказы для отображения
                    list_orders(orders)

                case 'edit':
                    # Передаем список и сохраняем результат редактирования
                    orders = edit_order(orders)

                case 'delete':
                    # Передаем список и сохраняем результат после удаления
                    orders = remove_order(orders)

                case 'exit':
                    # Сохраняем перед выходом
                    save(file_path, orders)
                    print("💾 Изменения сохранены. До свидания!")
                    break

                case _:
                    print("❓ Неизвестная команда. Введите help для справки.")

    except KeyboardInterrupt:
        # Сохранение при принудительном закрытии (Ctrl+C)
        print("\n\n⚠️ Прерывание пользователем...")
        save(file_path, orders)
        print("💾 Данные экстренно сохранены.")

    except Exception as e:
        # Ловим критические ошибки, чтобы не потерять данные
        print(f"💥 Критическая ошибка: {e}")
        save(file_path, orders)


if __name__ == "__main__":
    start_menu()
