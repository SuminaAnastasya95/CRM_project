"""Парсинг аргументов/ команд"""

from datetime import date, datetime
import whois


def parss_create_order(args: list[str]):
    if not args:
        raise ValueError(
            "ERROR: Используй формат -  < title > amount= 123,22 email= <email> status=['new', 'in_progress', 'done', 'cancelled'] [tags=a, b, c] [due=YYYY-MM-DD]")
    title = args[0]
    try:
        amount = float(args[1].replace(',', '.'))
    except (ValueError, IndexError):
        raise ValueError("Сумма заказа должна быть числом (второй аргумент)")
    email_val = None
    due = None
    status, tags = "new", None
    for arg in args[2:]:
        if arg.startswith("email="):
            email = arg.split('=', 1)[1]
            email_val = email_validator(email)
        elif arg.startswith("due="):
            due_str = arg.split('=', 1)[1]
            try:
                due = pars_date(due_str)
            except ValueError:
                raise ValueError(f"Неверный формат даты: {due_str}")
    if not email_val:
        raise ValueError('Не передан обязательный параметр email')
    return title, amount, email_val, status, tags, due


def pars_date(date_str: str) -> date:
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError as e:
        raise ValueError(
            f"Неверный формат даты: '{date_str}'. Ожидается ГГГГ-ММ-ДД")


def email_validator(email: str):
    email = email.strip()
    if not email.count("@"):
        print("Не верный формат email. Отсутствует '@'")
        return None
    try:
        name, domain = email.split('@')
        if not name or not domain or '.' not in domain:
            raise ValueError(
                "Не верный формат домена. {name}/ {domen} не соответствует формату: test@test.ru")
        domain_info = whois.whois(domain)
        if not domain_info.domain_name:  # type: ignore
            print(f"Домен {domain} не зарегистрирован.")
            return None
    except ValueError as e:
        print(f"ERROR: Ошибка валидации- {e}")
        return None
    except Exception as e:
        print(f'Сетевая ошибка или домен не найден: {e}')
        return None
    return email


# print(parss_create_order(
#     ["Айпфон", '100', 'email= lal@google.com', 'due = 2025-12-31']))
