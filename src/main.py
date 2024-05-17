import pprint

from src.decorators import log
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date_new, get_masks_accounts_cards

# список словарей для processing.py
transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


# список словарей для generators.py
transactions1 = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


print(get_masks_accounts_cards("Visa Platinum 7000792289606361"))
# для разделения результата
print()

print(get_masks_accounts_cards("Счет 73654108430135874305"))
# для разделения результата
print()

print(get_date_new("2018-07-11T02:26:18.671407"))
# для разделения результата
print()

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
sorted_transactions = sort_by_date(transactions)
pp = pprint.PrettyPrinter()
pp.pprint(sorted_transactions)

# для разделения результата
print()

# Сортировка по возрастанию даты
sorted_transactions = sort_by_date(transactions, False)
pp = pprint.PrettyPrinter()
pp.pprint(sorted_transactions)
# для разделения результата
print()

usd_transactions = filter_by_currency(transactions1, "USD")
for _ in range(3):
    print(next(usd_transactions)["id"])
# для разделения результата
print()

descriptions = transaction_descriptions(transactions1)
for i in range(5):
    print(next(descriptions))
# для разделения результата
print()

for card_number in card_number_generator(1, 5):
    print(card_number)

# для разделения результата
print()


@log(filename="../mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)
