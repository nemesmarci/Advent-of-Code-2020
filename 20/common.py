import numpy as np
from itertools import product


class Tile:
    def __init__(self, num, data):
        self.num = num
        self.data = data
        self.neighbours = {0: None, 1: None, 2: None, 3: None}

    @property
    def sides(self):
        return [self.data[0], self.data[-1],
                self.data[:, 0], self.data[:, -1]]


def parse():
    tiles = {}
    with open('input.txt') as data:
        for tile in data.read().split('\n\n')[:-1]:
            t = tile.split('\n')
            num = t[0].split()[1].split(':')[0]
            lines = t[1:]
            tiles[num] = Tile(num, np.array(list([c for c in line]
                                                 for line in lines)))
    for name in tiles:
        curr = tiles[name]
        for s in tiles:
            if s == name:
                continue
            other = tiles[s]
            for a, b in product(range(4), repeat=2):
                if (curr.sides[a] == other.sides[b]).all() \
                        or (curr.sides[a] == other.sides[b][::-1]).all():
                    curr.neighbours[a] = s
                    break
    return tiles


def is_corner(tile):
    return len([n for n in tile.neighbours.values() if n is not None]) == 2
