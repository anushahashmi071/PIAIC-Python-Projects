max_limit: int = 10000


def fibonacci() -> int:
    a, b = 0, 1
    while a < max_limit:
        print(a, end=',')
        a, b = b, a+b


fibonacci()
