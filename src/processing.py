from typing import Dict, List


def filter_by_state(list_dict: list, value_key: str = "EXECUTED") -> List[Dict]:
    """функция возвращает новый список словарей, у которых ключ state
    соответствует указанному значению, по умолчанию 'EXECUTED'
    """
    new_list_dict = []
    for every_dict in list_dict:
        if every_dict["state"] == value_key:
            new_list_dict.append(every_dict)
    return new_list_dict  # возвращает отсортированный список


def sort_by_date(list_dict: list, arg_for_sort: bool = True) -> List[Dict]:
    """ Функция возвращает отсортированный по убыванию даты список"""
    sort_list = sorted(list_dict, key=lambda every_dict: every_dict["date"], reverse=arg_for_sort)
    return sort_list  # возвращает отсортированный список по дате
