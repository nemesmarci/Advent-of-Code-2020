from math import prod

from common import solve


def solver(string):
    return(str(prod(sum(map(int, x.split(' + ')))
                    for x in string.split(' * '))))


print(solve(solver))
