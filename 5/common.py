KEYS = {'F': '0', 'L': '0', 'B': '1', 'R': '1'}


def bsp2int(sequence):
    for k, v in KEYS.items():
        sequence = sequence.replace(k, v)
    return int(sequence, 2)


def seat_id(line):
    line = line.strip()
    row = bsp2int(line[:7])
    col = bsp2int(line[-3:])
    return row * 8 + col
