import pprint
from src.processing import filter_by_state, sort_transactions_by_date

transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Вызов функции со статусом по умолчанию 'EXECUTED'
executed_transactions = filter_by_state(transactions)
pp = pprint.PrettyPrinter()
pp.pprint(executed_transactions)

# для разделения результата
print()

# Вызов функции с переданным статусом 'CANCELED'
canceled_transactions = filter_by_state(transactions, "CANCELED")
pp = pprint.PrettyPrinter()
pp.pprint(canceled_transactions)

# для разделения результата
print()

# Сортировка по убыванию даты
sorted_transactions = sort_transactions_by_date(transactions)
pp = pprint.PrettyPrinter()
pp.pprint(sorted_transactions)

# для разделения результата
print()

# Сортировка по возрастанию даты
sorted_transactions = sort_transactions_by_date(transactions, order=False)
pp = pprint.PrettyPrinter()
pp.pprint(sorted_transactions)
