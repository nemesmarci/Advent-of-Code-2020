from itertools import combinations
from functools import reduce
from operator import mul


def solve(n):
    with open('input.txt') as data:
        return (next(reduce(mul, combination)
                     for combination in combinations(map(int, data), n)
                     if sum(combination) == 2020))
