from common import Seats


def count_neighbours(location, seats):
    ly, lx = location
    return sum(neighbour in seats and seats[neighbour] == '#'
               for neighbour in ((y, x)
                                 for x in range(lx - 1, lx + 2)
                                 for y in range(ly - 1, ly + 2)
                                 if (y, x) != (ly, lx)))


print(Seats(count_neighbours, 4).run())
