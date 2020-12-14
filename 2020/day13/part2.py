from functools import reduce
from typing import List, Tuple

FILE_IN = "day13.in"
# FILE_IN = "test.in"


def main() -> None:
    remainders, modulo = ingest()
    print("remainders", remainders)
    print("modulo", modulo)
    print(chinese_remainder(modulo, remainders))


def chinese_remainder(remainers: List[int], modulos: List[int]) -> int:
    sum = 0
    prod = reduce(lambda a, b: a * b, remainers)
    for n_i, a_i in zip(remainers, modulos):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return abs((sum % prod) - prod)


def mul_inv(a: int, b: int) -> int:
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def ingest() -> Tuple[List[int], List[int]]:
    lines = [x.rstrip() for x in open(FILE_IN).readlines()]
    remainders = []
    modulo = []

    for index, value in enumerate(lines[1].split(",")):
        if value == "x":
            continue
        remainders.append(index)
        modulo.append(int(value))

    return remainders, modulo


if __name__ == "__main__":
    main()
