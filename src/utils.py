import json


def get_transactions(file_path: str) -> list[dict]:
    """
    Функция, которая принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            repos = json.load(file)
            if isinstance(repos, list):
                return repos
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
