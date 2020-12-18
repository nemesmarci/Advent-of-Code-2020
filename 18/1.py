from common import solve


def solver(string):
    operand1 = None
    operand2 = ''
    operator = None
    for c in string + 'x':  # add 'x' so we evaluate at the end too
        if c == ' ':
            continue
        if c not in '+*x':
            operand2 += c
        else:
            operand2 = int(operand2)
            if operand1 is None:
                operand1 = operand2
            else:
                if operator == '*':
                    operand1 *= operand2
                else:
                    operand1 += operand2
            operator = c
            operand2 = ''
    return str(operand1)


print(solve(solver))
