from typing import Dict, List, Union

import pytest


@pytest.fixture
def uncorrect_info() -> str:
    return "Неверные данные!"


@pytest.fixture
def account_card() -> str:
    return "Счет **7890"


@pytest.fixture
def bad_date() -> str:
    return "Неверный формат даты!"


@pytest.fixture
def filtred_list_state() -> List[Dict[str, Union[int, str]]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def filtred_list_date() -> List[Dict[str, Union[int, str]]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def filter_by_curr():
    return ({
        "id": 939719570, "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount":
            {
                "amount": "9824.07",
                "currency":
                    {
                        "name": "USD",
                        "code": "USD"
                    }
            },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
        {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount":
            {
                "amount": "79114.93",
                "currency":
                    {
                        "name": "USD",
                        "code": "USD"
                    }
            },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"})


@pytest.fixture
def description():
    return "Перевод организации"
    "Перевод со счета на счет"
    "Перевод со счета на счет"
    "Перевод с карты на карту"
    "Перевод организаци"
