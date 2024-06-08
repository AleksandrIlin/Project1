# Project1
## Функции проекта
### get_mask_cards
    """Функция возвращает маску карты"""

### get_mask_account
    """Функция возвращает маску счёта"""

### get_masks_accounts_cards
    """Функция получает строку и маскирует номер карты или счёта"""

### get_date_new
    """Функция принимает строку и выводит дату."""

### filter_by_state
    """Функция принимает на вход список словарей и значение для ключа 'state'
    (опциональный параметр со значением по умолчанию 'EXECUTED')
    и возвращает новый список, содержащий только те словари, у которыx 'state' 
    содержит переданное в функцию значение."""

### sort_by_date
    """Функция использует встроенную функцию `sorted()` для сортировки списка словарей по дате"""

### filter_by_currency
    """Функция принимает список словарей и возвращает итератор, который выдаёт по очереди операции,
    в указанной валюте."""
### transaction_descriptions
    """Генератор, который принимает список словарей и возвращает описание каждой операции по очереди."""
### card_number_generator
    """Генератор номеров банковских карт, который генерирует номера карт"""
### def log
    """Декоратор записывающий выполнение функции в файл mylog.txt"""

# transactions
    transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
# transactions1
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
# Виджет для отслеживания банковских операций клиента
# Имеет функции:
1. Маскировка номера карты
2. Маскировка номера счёта
3. Фильтрация списка операций
4. Вывод даты
5. Сортировка по дате
6. Итератор, который выдаёт операции в указанной валюте
7. Генератор, который возвращает описание каждой операции
8. Генератор номеров банковских карт
9. Декоратор
10. Преобразование файла Json в объект Python
11. Конвертация валюты из транзакций
12. Добавлено логирование файла masks & utils 
## Для запуска проект запустите [main](https://github.com/Dimon4ik812/homework/blob/feature/homework_10_1/main.py)
## Проект покрыт юнит-тестами. Для запуска выполните команду:
```
pytest --cov
```