import json
import logging


logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/utils.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions(file_path: str) -> list[dict]:
    """
    Функция, которая принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        logger.info(f'открываем json файл {file_path}')
        with open(file_path, "r", encoding="utf-8") as file:
            repos = json.load(file)
            logger.info(f'Проверяем что файл не пустой')
            if isinstance(repos, list):
                logger.info(f'Возвращаем объект python ')
                return repos
            else:
                logger.info(f'Возвращаем пустой словарь если файл {file_path} пустой')
                return []
    except Exception as e:
        logger.error(f'Ошибка {e}')
        return []
