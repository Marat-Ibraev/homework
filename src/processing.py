from typing import Any, Dict, List


def filter_by_state(list_dict: list, value_key: str = "EXECUTED") -> List[dict]:
    """функция возвращает новый список словарей, у которых ключ state
    соответствует указанному значению, по умолчанию 'EXECUTED'
    """
    new_list_dict = []
    for every_dict in list_dict:
        if every_dict["state"] == value_key:
            new_list_dict.append(every_dict)
    return new_list_dict  # возвращает отсортированный список


def sort_by_date(
    user_input: List[Dict[str, Any]], reverse: bool = True
) -> List[Dict[str, Any]]:
    """
    Функция, которая возвращает список отсортированный по дате.
    """
    sort_date = sorted(user_input, key=lambda x: x["date"], reverse=reverse)
    return sort_date  # возвращает список отсортированный по дате
