from common import solve


def in_range(lower, upper, char, password):
    return lower <= password.count(char) <= upper


print(solve(validator=in_range))
