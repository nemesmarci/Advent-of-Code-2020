from functools import reduce
from operator import mul

from common import get_jolts, get_diffs


def tribo(n):
    return tribo(n-1) + tribo(n-2) + tribo(n-3) if n > 2 \
        else 1 if n == 0 else n


diffs = map(len, ''.join(map(str, get_diffs(get_jolts()))).split('3'))
print(reduce(mul, map(tribo, diffs)))
