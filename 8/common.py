def run(code, j=None):
    acc = 0
    pc = 0
    seen = set()
    while True:
        if pc >= len(code):
            return acc, True
        if pc in seen:
            return acc, False
        instr, op = code[pc]
        seen.add(pc)
        if instr == 'nop' or (pc == j and instr == 'jmp'):
            pass
        elif instr == 'acc':
            acc += op
        elif instr == 'jmp' or (pc == j and instr == 'nop'):
            pc += op - 1
        pc += 1


def parse():
    with open('input.txt') as data:
        return [[instr, int(op)] for instr, op in (map(str.split, data))]
