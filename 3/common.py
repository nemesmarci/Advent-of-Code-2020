from math import prod


def solve(slopes):
    with open('input.txt') as data:
        lines = [line.strip() for line in data]
    height = len(lines)
    width = len(lines[0])

    trees = []
    for slope in slopes:
        right = slope[0]
        down = slope[1]
        x, y = 0, 0
        n = 0
        while y < height:
            if lines[y][x] == '#':
                n += 1
            x += right
            x %= width
            y += down
        trees.append(n)
    return prod(trees)
