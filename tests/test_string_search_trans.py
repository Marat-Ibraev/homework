from collections import Counter

from src.string_search_trans import count_trans, search_trans


def test_search_transactions_found(sample_transactions):
    result = search_trans(sample_transactions, "Перевод")
    assert len(result) == 3
    assert all("Перевод" in item["description"] for item in result)


def test_search_transactions_not_found(sample_transactions):
    result = search_trans(sample_transactions, "Невозможно найти")
    assert result == []


def test_count_transactions(sample_transactions, sample_categories):
    result = count_trans(sample_transactions, sample_categories)
    expected = Counter({"Оплата": 4, "Переводы": 3, "Списание кредитов": 1})
    assert result == expected
