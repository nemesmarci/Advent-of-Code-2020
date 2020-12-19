from common import parse, count_matches

rules, strings = parse()

rules['8'] = ' | '.join((' '.join(['42'] * i)
                        for i in range(1, 6))).split()

rules['11'] = ' | '.join((' '.join(['42'] * i + ['31'] * i))
                         for i in range(1, 6)).split()

print(count_matches(rules, strings))
