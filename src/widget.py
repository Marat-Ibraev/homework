from typing import Union

from src.masks import get_mask_account, get_mask_card_number

user_input = input("Введите данные ")


def mask_account_card(user_input: Union[str.split[], int.split[]]) -> Union[str.split[], int.split[]]:
    """
    маскировка данных
    """
    if user_input.split(" ")[0] == "Счет":
        result = get_mask_account(user_input)
        return f"{user_input.split(" ")[0]} {result}"
    elif user_input.split(" ")[0] != "Счет" and len(user_input.split(" ")) in [2, 3]:
        if len(user_input.split(" ")) == 2:
            type_card = user_input.split(" ")[0]
            number_card = get_mask_card_number(user_input.split(" ")[-1])
        elif len(user_input.split(" ")) == 3:
            type_card = " ".join([user_input.split(" ")[0], user_input.split(" ")[1]])
            number_card = get_mask_card_number(user_input.split(" ")[-1])
    return f"{type_card} {number_card}"


date_user_input = input("Введите дату ")


def get_date(date_user_input: Union[str, int]) -> None:
    """
    обработка даты
    """
    day = date_user_input[8:10]
    mounth = date_user_input[5:7]
    year = date_user_input[0:4]
    full_date = ".".join([day, mounth, year])
    return full_date
