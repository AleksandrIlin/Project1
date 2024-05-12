def get_mask_cards(number: str) -> str:
    """Функция возвращает маску карты"""
    if len(number) > 0:
        if len(number) == 16:
            result = f"{number[0:4]} {number[4:6]}** **** {number[12:]}"
            return result
        else:
            return ""
    return ""


def get_mask_account(number: str) -> str:
    """Функция возвращает маску счёта"""
    if len(number) > 0:
        if len(number) == 20:
            result = f"**{number[-4:]}"
            return result
        else:
            return ""
    return ""
