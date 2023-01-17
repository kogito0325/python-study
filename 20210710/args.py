# args, kwargs

print('Hello,', 'World!')
print('Hello, World!')


def f(*args: int) -> int:
    sum_ = 0
    for value in args:
        sum_ += value
    return sum_


print(f(1, 2, 3, 4, 5))
