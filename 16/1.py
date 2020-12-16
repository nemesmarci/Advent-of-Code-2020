from common import parse, match_rule

rules, _, others = parse()

print(sum(field for ticket in others for field in ticket
          if not any(match_rule(field, rules[rule]) for rule in rules)))
