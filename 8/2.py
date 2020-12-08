from common import parse, run


code = parse()
print(next(result[0] for i in range(len(code)) if (result := run(code, i))[1]))
