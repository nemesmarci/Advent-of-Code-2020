from common import find_blacks


def neighbours(tile):
    x, y, z = tile
    return [(x, y+1, z-1), (x+1, y, z-1), (x+1, y-1, z),
            (x, y-1, z+1), (x-1, y, z+1), (x-1, y+1, z)]


def count_blacks(tile, blacks):
    return sum(n in blacks for n in neighbours(tile))


blacks = find_blacks()

for _ in range(100):
    to_add = set()
    to_remove = set()
    for black in blacks:
        if (count := count_blacks(black, blacks)) == 0 or count > 2:
            to_remove.add(black)
        for white in (n for n in neighbours(black) if n not in blacks):
            if count_blacks(white, blacks) == 2:
                to_add.add(white)
    blacks -= to_remove
    blacks |= to_add

print(len(blacks))
