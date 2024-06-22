def filter_by_state(records, state='EXECUTED'):
    """
    Функция принимает список словарей и возвращает новый список,
    содержащий только те словари, у которых ключ 'state' содержит значение state.
    """
    return [record for record in records if record.get('state') == state]

# Пример использования функции
records = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Вызов функции с параметром по умолчанию
executed_records = filter_by_state(records)
print(executed_records)

# Вызов функции с параметром 'CANCELED'
canceled_records = filter_by_state(records, 'CANCELED')
print(canceled_records)
