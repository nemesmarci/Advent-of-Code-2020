def parse():
    with open('input.txt') as data:
        timestamp = int(data.readline())
        buses = [(i, int(id_)) for i, id_
                 in enumerate(data.readline().split(','))
                 if id_ != 'x']
        return timestamp, buses
