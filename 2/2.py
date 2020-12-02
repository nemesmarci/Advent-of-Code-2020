from common import solve


def at_position(pos1, pos2, char, password):
        return (password[pos1 - 1], password[pos2 - 1]).count(char) == 1


print(solve(validator=at_position))
