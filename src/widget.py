from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_account_number: Union[str]) -> str:
    """
    маскировка данных
    """
    first_word = card_account_number.split(" ")[0]
    masked_nums = card_account_number.split(" ")[-1]
    chek_words = len(card_account_number.split(" "))
    if first_word == "Счет":
        result = get_mask_account(masked_nums)
        return f"{first_word} {result}"  # возвращает замаскированный счет
    elif first_word != "Счет" and chek_words in [2, 3]:
        if chek_words == 2:
            type_card = first_word
        elif chek_words == 3:
            type_card = " ".join([first_word, card_account_number.split(" ")[1]])
        number_card = get_mask_card_number(masked_nums)
        if number_card == "Неверные данные!":
            return number_card
        result = " ".join([type_card, number_card])
        return result  # возвращает замаскированную карту
    else:
        return "Неверные данные!"


def get_date(date_user_input: Union[str]) -> str:
    """
    обработка даты
    """
    if len(date_user_input) == 26:
        day = date_user_input[8:10]
        mounth = date_user_input[5:7]
        year = date_user_input[0:4]
        full_date = ".".join([day, mounth, year])
        return full_date
    else:
        return "Неверный формат даты!"
