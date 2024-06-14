import os

from src.logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "../logs", "masks.log")
logger = setup_logger("masks", file_path)


def get_mask_cards(number: str) -> str:
    """Функция возвращает маску карты"""
    logger.info(f"Проверяем {number} что он > 0")
    if len(number) > 0:
        logger.info(f"Проверяем что {number} равен 16 символам")
        if len(number) == 16:
            logger.info(f"Маскируем {number} согласно условия задачи")
            result = f"{number[0:4]} {number[4:6]}** **** {number[12:]}"
            logger.info(f"Выводим результат маскировки {result}")
            return result
        else:
            logger.info(f"Выводим результат если {number} не равен 16 символам")
            return ""
    logger.info(f"Выводим результат если {number} меньше или равен нулю")
    return ""


def get_mask_account(number: str) -> str:
    """Функция возвращает маску счёта"""
    logger.info(f"Проверяем {number} что он > 0")
    if len(number) > 0:
        logger.info(f"Проверяем что {number} равен 20 символам")
        if len(number) == 20:
            logger.info(f"Маскируем {number} согласно условия задачи")
            result = f"**{number[-4:]}"
            return result
        else:
            logger.info(f"Выводим пустой список если {number} не равен 20 символам")
            return ""
    logger.info(f"Выводим пустой список если {number} меньше или равен нулю")
    return ""
