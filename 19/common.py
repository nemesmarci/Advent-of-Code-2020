import re


def parse():
    rules = {}
    strings = []
    with open('input.txt') as data:
        in_rules = True
        for line in map(str.strip, data):
            line = line.replace('"', '')
            if line == '':
                in_rules = False
            elif in_rules:
                num, rule = line.strip().split(': ')
                rules[num] = rule.split()
            else:
                strings.append(line.strip())
    return rules, strings


def resolve(rule, rules):
    resolved = []
    for token in rules[rule]:
        if token in ('a', 'b', '|') or isinstance(token, list):
            resolved.append(token)
        else:
            rules[token] = resolve(token, rules)
            resolved.append(rules[token])
    return resolved


def regex(rule):
    return re.compile('^{}$'.format(
        repr(rule).replace(' ', '')
                  .replace(',', '')
                  .replace("'", '')
                  .replace("[", "(")
                  .replace("]", ")")))


def count_matches(rules, strings):
    return sum(regex(resolve('0', rules)).match(string)is not None
               for string in strings)
