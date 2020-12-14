from itertools import product

from common import solve, int2bin


def write_memory(addr, value, mask, memory):
    addr = int2bin(addr)
    for i, c in enumerate(mask):
        if c in 'X1':
            addr[i] = c
    c = addr.count('X')
    addr = ''.join(addr).replace("X", "{}")
    for x in product("01", repeat=c):
        memory[addr.format(*x)] = value


print(solve(write_memory))
