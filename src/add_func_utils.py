import pandas as pd


def transaction_csv_utils(transactions: list) -> list[dict]:
    """Обрабатывает словарь полученный из file.csv и добавляет в него ключ 'operationAmount'
    для корректной работы функции convert_to_rub"""
    data_list = []
    for transaction in transactions:
        if transaction["id"] != "":
            result = {
                "id": int(transaction["id"]),
                "state": transaction["state"],
                "date": transaction["date"],
                "operationAmount": {
                    "amount": float(transaction["amount"]),
                    "currency": {"name": transaction["currency_name"], "code": transaction["currency_code"]},
                },
                "description": transaction["description"],
                "from": transaction["from"],
                "to": transaction["to"],
            }

        else:
            result = {}
        data_list.append(result)
    return data_list


def transaction_xlsx_utils(transactions: list) -> list[dict]:
    """Обрабатывает словарь полученный из file.xlsx и добавляет в него ключ 'operationAmount'
    для корректной работы функции convert_to_rub"""
    data_list = []
    for transaction in transactions:
        if pd.notnull(transaction["id"]):
            result = {
                "id": int(transaction["id"]),
                "state": transaction["state"],
                "date": transaction["date"],
                "operationAmount": {
                    "amount": float(transaction["amount"]),
                    "currency": {"name": transaction["currency_name"], "code": transaction["currency_code"]},
                },
                "description": transaction["description"],
                "from": transaction["from"],
                "to": transaction["to"],
            }
            data_list.append(result)
        else:
            result = {}
            data_list.append(result)
    return data_list
