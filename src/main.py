import datetime
import os
import pandas as pd
from typing import Any
from src.processing import filter_by_state, sort_by_date
from src.utils import get_transactions, get_transactions_filter_by_key, get_transactions_filter_by_rub
from src.widget import get_masks_accounts_cards


def main() -> Any:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input("Введите номер пункта: ")

        if choice == "1":
            print("Для обработки выбран JSON-файл.")
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, "../data", "operations.json")
            transactions = get_transactions(file_path)
            break
        elif choice == "2":
            print("Для обработки выбран CSV-файл.")
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, "../data", "transactions.csv")
            transactions = get_transactions(file_path)
            break
        elif choice == "3":
            print("Для обработки выбран XLSX-файл.")
            current_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_dir, "../data", "transactions_excel.xlsx")
            transactions = get_transactions(file_path)
            break

        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    while True:
        choice = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. "
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:\n"
        )
        if choice.upper() == "CANCELED":
            transactions = filter_by_state(transactions, "CANCELED")

            break
        elif choice.upper() == "PENDING":
            transactions = filter_by_state(transactions, "PENDING")

            break
        elif choice.upper() == "EXECUTED":
            transactions = filter_by_state(transactions)
            # print(transactions)
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    while True:
        user_input = input("Отсортировать операции по дате?  Да/Нет\n").lower()
        if user_input == "да":
            if (
                input("Отсортировать по возрастанию или по убыванию?  по возрастанию/по убыванию\n").lower()
                == "по возрастанию"
            ):
                transactions = sort_by_date(transactions, False)
                break

            else:
                transactions = sort_by_date(transactions)
                break
        elif user_input == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    while True:
        user_input = input("Выводить только рублевые тразакции? Да/Нет\n").lower()
        if user_input == "да":
            transactions = get_transactions_filter_by_rub(transactions, "RUB")
            break
        elif user_input == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue
    while True:
        user_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет:\n").lower()
        if user_input == "да":
            search_key = input("Видите слово для поиска: ")
            transactions = get_transactions_filter_by_key(transactions, search_key)
            break
        elif user_input == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    if transactions == []:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    elif len(transactions) > 0:
        print(f"Всего банковских операций в выборке: {len(transactions)}")

    for transaction in transactions:
        date = datetime.datetime.fromisoformat(transaction["date"]).strftime("%d.%m.%Y")
        if pd.notnull(transaction["from"]):
            from_ = get_masks_accounts_cards(transaction["from"])
        else:
            from_ = "0"
        to_ = get_masks_accounts_cards(transaction["to"])
        description = transaction["description"]
        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["name"]
        print("Распечатываю итоговый список транзакций...")
        print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
