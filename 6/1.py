from common import parse_answers

print(sum(len(group[0]) for group in parse_answers()))
