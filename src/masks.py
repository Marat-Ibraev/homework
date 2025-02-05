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
        return correct_card_number
    else:
        return "Неверные данные!"


def get_mask_account(account_number: str) -> str:
    """
    функция, которая маскирует номер аккаунта
    """
    if len(account_number) == 20:
        account_number = account_number[-6:]
        account_number = account_number.replace(account_number[:2], "**")
        return account_number  # возвращает замаскированный номер аккаунта
    else:
        return "Неверные данные!"  # возвращает при неверном номере аккаунта
