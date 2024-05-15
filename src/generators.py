from typing import Dict, Generator, Iterator, List


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """Функция принимает список словарей и возвращает итератор, который выдаёт по очереди операции,
    в указанной валюте."""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Generator:
    """Генератор, который принимает список словарей и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генератор номеров банковских карт"""
    for number in range(start, end + 1):
        number_card = f"{number:016d}".replace(" ", "")
        format_number_card = " ".join([number_card[i:i + 4] for i in range(0, len(number_card), 4)])
        yield format_number_card
