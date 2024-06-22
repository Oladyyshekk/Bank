from datetime import datetime

def sort_records_by_date(records, order='descending'):
    """
    Функция принимает список словарей и возвращает новый список,
    отсортированный по дате в порядке убывания или возрастания.
    """
    return sorted(records, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=(order == 'descending'))

# Пример использования функции
records = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Вызов функции для сортировки по убыванию
sorted_records_desc = sort_records_by_date(records)
print(sorted_records_desc)


sorted_records_asc = sort_records_by_date(records, order='ascending')
print(sorted_records_asc)
