def parse():
    instructions = []
    with open('input.txt') as data:
        for line in data:
            addr, value = line.strip().split(' = ')
            if addr != 'mask':
                addr = int(addr[4:-1])
                value = int(value)
            instructions.append((addr, value))
    return instructions


def int2bin(num):
    num = bin(num).replace("0b", "")
    return list((36 - len(num)) * '0' + num)


def solve(write_memory):
    instructions = parse()
    memory = dict()
    mask = 32*'X'
    for instr in instructions:
        if instr[0] == 'mask':
            mask = instr[1]
        else:
            addr, value = instr
            write_memory(addr, value, mask, memory)
    return sum(memory.values())
