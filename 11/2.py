from common import Seats


def count_neighbours(location, tiles):
    ly, lx = location
    occupied = 0
    for diry in (-1, 0, 1):
        for dirx in (-1, 0, 1):
            if dirx == diry == 0:
                continue
            cy, cx = ly + diry, lx + dirx
            while (cy, cx) in tiles:
                if tiles[cy, cx] == 'L':
                    break
                if tiles[cy, cx] == '#':
                    occupied += 1
                    break
                cx, cy = cx + dirx, cy + diry
    return occupied


print(Seats(count_neighbours, 5).run())
