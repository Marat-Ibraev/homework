import os
from typing import Any
from webbrowser import Error

import requests
from dotenv import load_dotenv

load_dotenv('.env_example')

API_KEY = os.getenv("API_KEY")


def convert_current(currency, rub, amount) -> Any:
    """ Функция обращается к внешнему API и производит конвертацию валюты. """
    response = requests.get(
        f"https://api.apilayer.com/exchangerates_data/convert?to="
        f"{rub}&from={currency}&amount={amount}&apikey={API_KEY}")

    if response.status_code == 200:
        currency_rate = response.json()['info']['rate']
        result = response.json()['result']
        print(f"\nКонвертация валюты из {currency} в {rub} по курсу: {currency_rate}")
        return result
    else:
        print("\nОшибка запроса конвертации валюты.")
        return Error
