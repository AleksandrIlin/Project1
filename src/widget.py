from src.masks import get_mask_account, get_mask_cards


def get_masks_accounts_cards(str_number: str) -> str:
    """Функция получает строку и маскирует номер карты или счёта"""
    if len(str_number) > 0:
        if len(str_number.split()[-1]) == 16:
            result = get_mask_cards(str_number.split()[-1])
            str_mask_card = f"{str_number[:-16]}{result}"
            return str_mask_card
        elif len(str_number.split()[-1]) == 20:
            result = get_mask_account(str_number.split()[-1])
            str_mask_account = f"{str_number[:-20]}{result}"
            return str_mask_account
    else:
        return ""
    return ""


def get_date_new(data_string: str) -> str:
    """Функция принимает строку и выводит дату."""
    if len(data_string) > 0:
        if len(data_string) == 26:
            result = data_string[:10].split("-")
            new_data = ".".join(result[::-1])
            return new_data
        else:
            return ""
    return ""
