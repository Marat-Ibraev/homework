from typing import Any

import pytest

from src.decorators import log


@log()
def good_func(x: int, y: int) -> int:
    return x + y


@log()
def bad_func(x: int, y: int) -> float:
    return x / y


def test_good_func(capsys: Any) -> None:
    good_func(3, 4)
    captured = capsys.readouterr()
    assert "good_func ok. Result: 7" in captured.out


def test_bad_func(capsys: Any) -> None:
    with pytest.raises(ZeroDivisionError):
        bad_func(1, 0)
        captured = capsys.readouterr()
        assert "bad_func error: division by zero" in captured.out
        assert "input: (1, 0), {}" in captured.out


def test_log_to_file(tmp_path: Any) -> None:
    log_file = tmp_path / "test_log.txt"
    func = log(filename=str(log_file))(good_func)
    func(5, 7)
    with open(log_file) as f:
        log_contents = f.read()

    assert "good_func ok. Result: 12" in log_contents


def test_error_log_to_file(tmp_path: Any) -> None:
    log_file = tmp_path / "test_error_log.txt"
    func = log(filename=str(log_file))(bad_func)

    with pytest.raises(ZeroDivisionError):
        func(1, 0)

    with open(log_file) as f:
        log_contents = f.read()

    assert "bad_func error: division by zero" in log_contents
    assert "Inputs: (1, 0), {}" in log_contents
