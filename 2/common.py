import re


RE = re.compile(r'(\d+)-(\d+) (\w): (\w+)')


def parse(line):
    num1, num2, char, password = re.match(RE, line).groups()
    return int(num1), int(num2), char, password


def solve(validator):
    with open('input.txt') as data:
        return(sum(validator(*parse(line)) for line in data))
