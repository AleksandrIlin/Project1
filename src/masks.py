def get_mask_cards(number: str) -> str:
    """Функция возвращает маску карты"""
    result = f"{number[0:4]} {number[4:6]}** **** {number[12:]}"
    return result


def get_mask_account(number: str) -> str:
    """Функция возвращает маску счёта"""
    result = f"**{number[-4:]}"
    return result
