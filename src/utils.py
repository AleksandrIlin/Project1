import csv
import json
import os
import re
from typing import Any

import pandas
import pandas as pd
from src.add_func_utils import transaction_csv_utils, transaction_xlsx_utils
from src.logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "utils.log")

logger = setup_logger("utils", file_path_1)


def get_transactions(file_path: str) -> list[dict]:
    """
    Функция, которая принимает путь до файла и возвращает список словарей с данными.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        if file_path.endswith(".json"):
            logger.info(f"открываем json файл {file_path}")
            with open(file_path, "r", encoding="utf-8") as file:
                repos = json.load(file)
                logger.info(f"Проверяем что {file_path} не пустой")
                if isinstance(repos, list):
                    logger.info("Возвращаем объект python repos")
                    return repos
                else:
                    logger.info(f"Возвращаем пустой словарь если файл {file_path} пустой")
                    return []
        elif file_path.endswith(".csv"):
            logger.info(f"Проверяем имеет ли переданный {file_path} расширение .csv")
            data_list: list[Any] = []
            logger.info(f"Создаем список  {data_list}.")
            logger.info(f"проверяем что {file_path} не пустой")
            if pd.read_csv(file_path).shape[0] > 0:
                logger.info(f"Читаем переданный {file_path}")
                with open(file_path, "r", encoding="utf-8") as file:
                    reader = csv.DictReader(file, delimiter=";")
                    logger.info("Создаем словари reader")
                    logger.info("Перебираем полученные словари reader через цикл для создания списка словарей")
                    for row in reader:
                        data_list.append(row)
                logger.info(
                    "Обрабатываем полученный список словарей data_list для корректного вида"
                    "с помощью функции transaction_csv_utils"
                )
                data_list2 = transaction_csv_utils(data_list)
                logger.info("Возвращаем список словарей data_list2")
                return data_list2
            else:
                return []
        elif file_path.endswith(".xlsx"):
            logger.info(f"Проверяем имеет ли переданный {file_path} расширение .xlsx")
            logger.info(f"Открываем xlsx файл {file_path}")
            with open(file_path, "rb") as file:
                dataframe_xlsx = pd.read_excel(file)
                logger.info("Создаем dataframe_xlsx")
                logger.info("Проверяем что создался файл dataframe_xlsx")
                if isinstance(dataframe_xlsx, pandas.DataFrame):
                    logger.info("Преобразуем dataframe_xlsx в список словарей")
                    list_of_dicts = dataframe_xlsx.to_dict("records")
                    logger.info(
                        "Обрабатываем полученный список словарей list_of_dicts для корректного вида "
                        "с помощью функции transaction_xlsx_utils"
                    )
                    list_of_dicts2 = transaction_xlsx_utils(list_of_dicts)
                    return list_of_dicts2

                else:
                    return []
        else:
            return []

    except Exception as e:
        logger.error(f"Ошибка {e}")
        print(f"ошибка {e}")
        return []


def get_transactions_filter_by_key(transactions: list, search_key: str) -> list:
    """Функцию, которая принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей"""
    result = []
    for transaction in transactions:
        if "description" in transaction and re.search(search_key, transaction["description"], re.IGNORECASE):
            result.append(transaction)
    return result


def get_transactions_filter_by_rub(transactions: list, search_key: str) -> list:
    """Функция фильтрации транзакций по коду валюты"""
    result = []
    for transaction in transactions:
        if (
            "operationAmount" in transaction
            and "currency" in transaction["operationAmount"]
            and re.search(search_key, transaction["operationAmount"]["currency"]["code"], re.IGNORECASE)
        ):
            result.append(transaction)
    return result


def get_transactions_by_category(transactions: list[dict], categories: dict) -> dict:
    """
    Принимает список словарей с данными о банковских операциях и словарь категорий операций.
    Возвращает словарь, в котором ключи - это названия категорий, а значения - количество операций в каждой категории.
    """

    category_counts = {category: 0 for category in categories}

    for transaction in transactions:
        if "description" in transaction:
            for category in categories:
                if category.lower() in transaction["description"].lower():
                    category_counts[category] += 1

    return category_counts
