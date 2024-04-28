# Декоратор для хронометража сопрограмм
import functools
import time
from typing import Callable, Any


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'{func} is running with arguments {args}, {kwargs}')
            start = time.time()

            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'It took {func} {total:.4f} s to s.')

        return wrapped
    return wrapper

