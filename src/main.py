import widget
def mask_card_number(card_number):
    """Функция для номера карты"""
    if len(card_number) == 16 and card_number.isdigit():  # Проверяем, что номер карты состоит из 16 цифр
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"  # Возвращаем маскированный номер карты
    else:
        return "Неверный формат номера карты"

def mask_account_number(account_number):
    """Функция для номера счета"""
    if len(account_number) >= 4 and account_number.isdigit():  # Проверяем, что номер счета состоит из минимум 4 цифр
        return f"**{account_number[-4:]}"  # Возвращаем маскированный номер счета
    else:
        return "Неверный формат номера счета"


card_num = "1234567890123456"
account_num = "12345678"

print(mask_card_number(card_num))  # Вывод: 1234 56** **** 3456
print(mask_account_number(account_num))  # Вывод: **5678
