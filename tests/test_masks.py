import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("124124124", "Неверные данные!"),
        ("^&*$#", "Неверные данные!"),
    ],
)
def test_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


def test_mask_card_number_fixture(uncorrect_info: str) -> None:
    assert get_mask_card_number("0") == uncorrect_info


@pytest.mark.parametrize(
    "account_num, expected",
    [
        ("73654108430135874305", "**4305"),
        ("2222", "Неверные данные!"),
    ],
)
def test_get_mask_account(account_num: str, expected: str) -> None:
    assert get_mask_account(account_num) == expected


def test_get_mask_account_fixture(uncorrect_info: str) -> None:
    assert get_mask_account("&@^%$") == uncorrect_info
