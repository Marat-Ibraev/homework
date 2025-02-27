import json

from src.external_api import convert_current

import logging


logger = logging.getLogger("utils_log")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils_log.log", "w", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

path = 'data/operations.json'


def convert_transactions(path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей"""
    logger.info("Работа со словарем")
    try:
        with open(path, encoding="utf-8") as transactions_file:
            try:
                transactions = json.load(transactions_file)
            except json.JSONDecodeError:
                logger.error("Ошибка декодирования файла")
                print("Ошибка декодирования файла")
                return []
    except FileNotFoundError:
        logger.error("Файл не найден")
        print("Файл не найден")
        return []
    logger.info(f"Результат: {transactions}")
    return transactions


def transaction_amount(transaction: dict) -> float:
    all_sum = 0
    logger.info("Суммируем все рубли и конвертируем доллары в рубли и их тоже суммируем")
    for i in transaction:
        try:
            currency = i["operationAmount"]["currency"]["code"]
            amount = i["operationAmount"]["amount"]
            if currency == "RUB":
                all_sum += float(amount)
            else:
                alternative_summ = convert_current(currency, "RUB", amount)
                if not alternative_summ == "Error":
                    all_sum += float(alternative_summ)
        except KeyError:
            logger.warning("Превышен результат запросов по api ключу")
            continue
    logger.info(f"Сумма всех транзакций: {all_sum}")
    return all_sum
