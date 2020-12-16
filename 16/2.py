from math import prod

from common import parse, match_rule

rules, my_fields, others = parse()

valid = tuple(ticket for ticket in others
              if all(any(match_rule(field, rules[rule]) for rule in rules)
                     for field in ticket))

possible_cols = [set(rules.keys()) for _ in range(len(valid[0]))]

while any(len(x) > 1 for x in possible_cols):
    for ticket in valid:
        for col, num in enumerate(ticket):
            possible_cols[col] = {rule for rule in possible_cols[col]
                                  if match_rule(num, rules[rule])}
            if len(to_remove := possible_cols[col]) == 1:
                for i, other in enumerate(possible_cols):
                    if i != col:
                        other -= to_remove

print(prod(my_fields[i] for i, col in enumerate(possible_cols)
           if 'departure' in col.pop()))
