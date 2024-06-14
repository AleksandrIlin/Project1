from src.add_func_utils import transaction_csv_utils, transaction_xlsx_utils


def test_transaction_csv_utils_empty() -> None:
    assert transaction_csv_utils([]) == []


def test_transaction_xlsx_utils_empty() -> None:
    assert transaction_csv_utils([]) == []


def test_transaction_csv_utils() -> None:
    assert transaction_csv_utils(
        [
            {
                "id": "4699552",
                "state": "EXECUTED",
                "date": "2022-03-23T08:29:37Z",
                "amount": "23423",
                "currency_name": "Peso",
                "currency_code": "PHP",
                "from": "Discover 7269000803370165",
                "to": "American Express 1963030970727681",
                "description": "Перевод с карты на карту",
            }
        ]
    ) == [
        {
            "id": 4699552,
            "state": "EXECUTED",
            "date": "2022-03-23T08:29:37Z",
            "operationAmount": {"amount": 23423.0, "currency": {"name": "Peso", "code": "PHP"}},
            "description": "Перевод с карты на карту",
            "from": "Discover 7269000803370165",
            "to": "American Express 1963030970727681",
        }
    ]


def test_transaction_xlsx_utils() -> None:
    assert transaction_xlsx_utils(
        [
            {
                "id": 4699552.0,
                "state": "EXECUTED",
                "date": "2022-03-23T08:29:37Z",
                "amount": 23423.0,
                "currency_name": "Peso",
                "currency_code": "PHP",
                "from": "Discover 7269000803370165",
                "to": "American Express 1963030970727681",
                "description": "Перевод с карты на карту",
            }
        ]
    ) == [
        {
            "id": 4699552,
            "state": "EXECUTED",
            "date": "2022-03-23T08:29:37Z",
            "operationAmount": {"amount": 23423.0, "currency": {"name": "Peso", "code": "PHP"}},
            "description": "Перевод с карты на карту",
            "from": "Discover 7269000803370165",
            "to": "American Express 1963030970727681",
        }
    ]
