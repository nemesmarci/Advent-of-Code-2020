from collections import Counter
from operator import add
from functools import reduce


def parse_answers():
    with open('input.txt') as data:
        return ((reduce(add, (Counter(person) for person in group)),
                 len(group))
                for group in map(str.split, data.read().split('\n\n')))
