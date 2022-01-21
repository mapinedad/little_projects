from time import time as t


def insertion_at_begin(data: list, n: int):
    start = t()
    for m in range(n):
        data.insert(0, None)
    end = t()
    print((end - start) / n)


def insertion_at_middle(data: list, n: int):
    start = t()
    for m in range(n):
        data.insert(n // 2, None)
    end = t()
    print((end - start) / n)


def insertion_at_end(data: list, n: int):
    start = t()
    for m in range(n):
        data.insert(n, None)
    end = t()
    print((end - start) / n)


data_test = list()

# insertion_at_end(data_test, 1000000)
# insertion_at_begin(data_test, 1000000)
# insertion_at_middle(data_test, 1000000)
