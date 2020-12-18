from string import ascii_lowercase


def evaluate(string, tokens, evaluated, solver):
    new_string = ''
    for c in string:
        if c not in ascii_lowercase:
            new_string += c
        else:
            if c not in evaluated:
                evaluated[c] = evaluate(tokens[c], tokens, evaluated, solver)
            new_string += evaluated[c]
    return solver(new_string)


def parse(string, solver):
    tokens = {}
    keys = iter(ascii_lowercase)
    while '(' in string:
        closed = string.find(')')
        opened = string.rfind('(', 0, closed)
        key = next(keys)
        tokens[key] = string[opened + 1: closed]
        string = string[:opened] + key + string[closed + 1:]
    return evaluate(string, tokens, {}, solver)


def solve(solver):
    with open('input.txt') as data:
        return sum(int(parse(line.strip(), solver)) for line in data)
