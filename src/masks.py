import logging


logger = logging.getLogger("masks_card_account")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/masks_card_account.log", "w", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    маскировка номера карты
    """
    if len(card_number) == 16:
        correct_card_number = " ".join(
            card_number[i * 4 : (i + 1) * 4] for i in range(4)
        ).split(" ")
        correct_card_number[1] = correct_card_number[1].replace(
            correct_card_number[1][2:], "**"
        )
        correct_card_number[2] = correct_card_number[2].replace(
            correct_card_number[2], "****"
        )
        correct_card_number = " ".join(correct_card_number)
        logger.info(f"Маскировка номера карты {correct_card_number}")
        return correct_card_number
    else:
        logger.error("Неверные данные")
        return "Неверные данные!"


def get_mask_account(account_number: str) -> str:
    """
    функция, которая маскирует номер аккаунта
    """
    if len(account_number) == 20:
        account_number = account_number[-6:]
        account_number = account_number.replace(account_number[:2], "**")
        logger.info(f"Маскировка номера аккаунта {account_number}")
        return account_number  # возвращает замаскированный номер аккаунта
    else:
        logger.error("Неверные данные")
        return "Неверные данные!"  # возвращает при неверном номере аккаунта
