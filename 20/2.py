import numpy as np
from math import sqrt

from common import parse, is_corner

tiles = parse()
width = int(sqrt(len(tiles)))
top_left = next(tile for tile in tiles.values() if is_corner(tile))


def fliplr(tile):
    tile.data = np.fliplr(tile.data)
    tile.neighbours[2], tile.neighbours[3] = \
        tile.neighbours[3], tile.neighbours[2]


def flipud(tile):
    tile.data = np.flipud(tile.data)
    tile.neighbours[0], tile.neighbours[1] = \
        tile.neighbours[1], tile.neighbours[0]


def rot90l(tile):
    tile.data = np.rot90(tile.data)
    tile.neighbours = {0: tile.neighbours[3],
                       1: tile.neighbours[2],
                       2: tile.neighbours[0],
                       3: tile.neighbours[1]}


def rot90r(tile):
    tile.data = np.rot90(tile.data, -1)
    tile.neighbours = {0: tile.neighbours[2],
                       1: tile.neighbours[3],
                       2: tile.neighbours[1],
                       3: tile.neighbours[0]}


if top_left.neighbours[1] is None:
    flipud(top_left)

if top_left.neighbours[3] is None:
    fliplr(top_left)

rows = []
first = top_left
for y in range(width):
    row = np.array(first.data[1:-1, 1:-1])
    curr = first
    for x in range(width - 1):
        right = tiles[curr.neighbours[3]]
        for b in range(4):
            if ((this := curr.sides[3]) == (that := right.sides[b])).all():
                if b == 0:
                    rot90l(right)
                    flipud(right)
                elif b == 1:
                    rot90r(right)
                elif b == 2:
                    pass
                elif b == 3:
                    fliplr(right)
                break
            elif (this == that[::-1]).all():
                if b == 0:
                    rot90l(right)
                elif b == 1:
                    rot90r(right)
                    flipud(right)
                elif b == 2:
                    flipud(right)
                elif b == 3:
                    flipud(right)
                    fliplr(right)
                break
        curr = right
        row = np.concatenate((row, curr.data[1:-1, 1:-1]), axis=1)
    rows.append(row)
    if y != width - 1:
        down = tiles[first.neighbours[1]]
        for b in range(4):
            if ((this := first.sides[1]) == (that := down.sides[b])).all():
                if b == 0:
                    pass
                elif b == 1:
                    flipud(down)
                elif b == 2:
                    rot90r(down)
                    fliplr(down)
                elif b == 3:
                    rot90l(down)
                break
            elif (this == that[::-1]).all():
                if b == 0:
                    fliplr(down)
                elif b == 1:
                    flipud(down)
                    fliplr(down)
                elif b == 2:
                    rot90r(down)
                elif b == 3:
                    rot90l(down)
                    fliplr(down)
                break
        first = down

picture = np.concatenate(rows, axis=0)

monster = ["                  # ",
           "#    ##    ##    ###",
           " #  #  #  #  #  #   "]

monster_hash = sum(line.count('#') for line in monster)

monster_x = len(monster[0])
monster_y = len(monster)
picture_x = len(picture[0])
picture_y = len(picture)

hash_count = sum(c == '#' for line in picture for c in line)


def find_monsters(picture):
    monsters_found = 0
    for y in range(picture_y - monster_y + 1):
        for x in range(picture_x - monster_x + 1):
            target = picture[y:y + monster_y, x:x + monster_x]
            if not any(c != target[i][j]
                       for i, line in enumerate(monster)
                       for j, c in enumerate(line) if c == '#'):
                for i, line in enumerate(monster):
                    for j, c in enumerate(line):
                        if c == '#':
                            picture[y + i][x + j] = 'O'
                monsters_found += 1
    return monsters_found


print(next(hash_count - monsters * monster_hash
           for flipped in (picture, np.fliplr(picture),
                           np.flipud(picture), np.flip(picture))
           for rotated in (flipped, np.rot90(flipped),
                           np.rot90(flipped, 2), np.rot90(flipped, 3))
           if (monsters := find_monsters(rotated))))
