from itertools import combinations
from math import prod


def solve(n):
    with open('input.txt') as data:
        return (next(prod(combination)
                     for combination in combinations(map(int, data), n)
                     if sum(combination) == 2020))
