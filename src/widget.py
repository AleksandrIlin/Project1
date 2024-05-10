from src.masks import get_mask_account, get_mask_cards


def get_masks_accounts_cards(str_number: str) -> str:
    """Функция получает строку и маскирует номер карты или счёта"""
    if len(str_number.split()[-1]) == 16:
        result = get_mask_cards(str_number.split()[-1])
        return f"{str_number[:-16]}{result}"
    elif len(str_number.split()[-1]) == 20:
        result = get_mask_account(str_number.split()[-1])
        return f"{str_number[:-20]}{result}"


def data_reverse(data_string: str) -> str:
    """Функция принимает строку и выводит дату"""
    data_result = data_string[:10]
    data_list = data_result.split("-")
    data_list.reverse()
    result = ".".join(data_list)
    return result
