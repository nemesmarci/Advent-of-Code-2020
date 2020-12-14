from common import solve, int2bin


def write_memory(addr, value, mask, memory):
    value = int2bin(value)
    for i, c in enumerate(mask):
        if c in '01':
            value[i] = c
    memory[addr] = int(''.join(value), 2)


print(solve(write_memory))
