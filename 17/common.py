from itertools import product


def read_data(dim):
    with open('input.txt') as data:
        activated = set()
        for y, line in enumerate(data):
            for x, c in enumerate(line.strip()):
                if c == '#':
                    point = [0] * dim
                    point[-2] = y
                    point[-1] = x
                    activated.add(tuple(point))
    return y + 1, x + 1, activated


class Cubes:
    def __init__(self, dim):
        self.dimensions = [[0, 0] for _ in range(dim)]
        self.dimensions[-2][1], self.dimensions[-1][1], self.activated = \
            read_data(dim)

    def count_neighbours(self, point):
        ranges = (range(coord - 1, coord + 2) for coord in point)
        return sum(neighbour in self.activated
                   for neighbour in product(*ranges)
                   if neighbour != point)

    def iterate(self):
        added = set()
        removed = set()
        ranges = (range(dim[0] - 1, dim[1] + 2) for dim in self.dimensions)
        for point in product(*ranges):
            current = '#' if point in self.activated else '.'
            if (neighbours := self.count_neighbours(point)) \
                    not in (2, 3) \
                    and current == '#':
                removed.add(point)
            elif neighbours == 3 and current == '.':
                added.add(point)
                for i, coord in enumerate(point):
                    if coord > self.dimensions[i][1]:
                        self.dimensions[i][1] = coord
                    elif coord < self.dimensions[i][0]:
                        self.dimensions[i][0] = coord
        self.activated -= removed
        self.activated |= added


def solve(dim):
    cubes = Cubes(dim)
    for _ in range(6):
        cubes.iterate()
    return len(cubes.activated)
