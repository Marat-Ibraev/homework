from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, логирующий работу функции и её результат в консоль"""

    def logging_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            try:
                result = func(*args, **kwargs)

                log_message = f"{func.__name__} ok. Result: {result}"

                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)
                return result
            except Exception as error_:
                log_message_1 = f"{func.__name__} error: {error_}, Inputs: {args}, {kwargs}"
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(log_message_1 + "\n")
                else:
                    print(log_message_1)
                raise
        return wrapper
    return logging_decorator
