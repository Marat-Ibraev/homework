import json

from src.external_api import convert_current

path = 'data/operations.json'


def convert_transactions(path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей"""
    try:
        with open(path, encoding="utf-8") as transactions_file:
            try:
                transactions = json.load(transactions_file)
            except json.JSONDecodeError:
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []

    return transactions


def transaction_amount(transaction: dict) -> float:
    """Функция возвращает сумму транзакции в рублях.
     Если транзакция была в USD или EUR, происходит обращение к внешнему API
     для получения текущего курса валют и конвертации суммы операции в рубли."""
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    if currency == "RUB":
        return amount
    else:
        result = convert_current(currency, "RUB", amount)
        return result
