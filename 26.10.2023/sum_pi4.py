from math import pi
from itertools import takewhile


def sum_and_check(max_denominator: int):
    """
    1/1 - 1/3 + 1/5 - 1/7 + 1/9 - ... = pi/4
    """
    num = sum(1/i - 1/(i + 2) for i in range(1, max_denominator, 4))
    pi4 = pi / 4
    signs_after_comma = sum(takewhile(
        lambda x: x,
        (i == j for (i, j) in zip(str(num)[2:], str(pi4)[2:]))
    ))
    print(f'Результат: {num}')
    print(f'Пи/4 = {pi4}')
    print(f'Число равно пи/4 с точностью до {signs_after_comma} знаков после запятой.')


sum_and_check(int(input('Знаменатели до: ')))
input()
