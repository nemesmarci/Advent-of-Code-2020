def parse(line):
    i = 0
    tokens = []
    while i < len(line) - 1:
        if line[i:].startswith('e'):
            tokens.append('e')
            i += 1
        elif line[i:].startswith('se'):
            tokens.append('se')
            i += 2
        elif line[i:].startswith('sw'):
            tokens.append('sw')
            i += 2
        elif line[i:].startswith('w'):
            tokens.append('w')
            i += 1
        elif line[i:].startswith('nw'):
            tokens.append('nw')
            i += 2
        elif line[i:].startswith('ne'):
            tokens.append('ne')
            i += 2
    return tokens


def find_blacks():
    blacks = set()
    with open('input.txt') as data:
        for line in data:
            tokens = parse(line)
            x, y, z = 0, 0, 0
            for token in tokens:
                if token == 'ne':
                    y += 1
                    z -= 1
                elif token == 'e':
                    x += 1
                    z -= 1
                elif token == 'se':
                    x += 1
                    y -= 1
                elif token == 'sw':
                    y -= 1
                    z += 1
                elif token == 'w':
                    x -= 1
                    z += 1
                elif token == 'nw':
                    x -= 1
                    y += 1
            if (x, y, z) in blacks:
                blacks.remove((x, y, z))
            else:
                blacks.add((x, y, z))
    return blacks
