from itertools import count


def read_data():
    with open('input.txt') as data:
        tiles = {}
        for y, line in enumerate(data):
            for x, c in enumerate(line.strip()):
                tiles[y, x] = c
    return y + 1, x + 1, tiles


class Seats:
    def __init__(self, count_neighbours, tolerance):
        self.count_neighbours = count_neighbours
        self.tolerance = tolerance
        self.height, self.width, self.tiles = read_data()
        self.occupied = 0

    def iterate(self):
        changed = 0
        to_change = {}
        for location in self.tiles:
            if (typ := self.tiles[location]) == '.':
                continue
            occupied = self.count_neighbours(location, self.tiles)
            if typ == '#':
                if occupied >= self.tolerance:
                    to_change[location] = 'L'
                    self.occupied -= 1
            elif typ == 'L':
                if occupied == 0:
                    to_change[location] = '#'
                    self.occupied += 1
        for changed in to_change:
            self.tiles[changed] = to_change[changed]
        return len(to_change)

    def run(self):
        return next(self.occupied for i in count()
                    if self.iterate() == 0)
