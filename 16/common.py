def to_ints(sep, string):
    return tuple(map(int, string.split(sep)))


def extract_ints(sep, iterable):
    return tuple(to_ints(sep, r) for r in iterable)


def parse():
    with open('input.txt') as data:
        raw_rules, my_ticket, others = data.read().split('\n\n')

    rules = {}
    for rule in raw_rules.split('\n'):
        name, ranges = rule.split(': ')
        rules[name] = extract_ints('-', ranges.split(' or '))

    my_fields = to_ints(',', my_ticket.split('\n')[1])

    others = extract_ints(',', others.split('\n')[1:-1])

    return rules, my_fields, others


def match_rule(num, rule):
    return rule[0][0] <= num <= rule[0][1] or rule[1][0] <= num <= rule[1][1]
