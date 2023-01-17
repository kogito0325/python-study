# decorator
from typing import Callable


def call_logger(logger_name: str):  # function
    def decorator(function):  # decorator
        def decorated(*args):  # function
            print(f'[{logger_name}] {function.__name__} called')
            return function(*args)
        return decorated
    return decorator


@call_logger('debug')
def repeat(function: Callable, count: int):
    for _ in range(count):
        function()


@call_logger('65431')
def f(x):
    return x + '2'


repeat(lambda: print(f('Hello, world!')), 10)
