import re

RE = re.compile(r'([NSEWLRF])(\d+)')


def instructions():
    instructions = []
    with open('input.txt') as data:
        for line in data:
            action, num = re.match(RE, line).groups()
            instructions.append([action, int(num)])
    return instructions


def manhattan(pos):
    return abs(pos[0]) + abs(pos[1])
