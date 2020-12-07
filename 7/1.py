from common import Rules

rules = Rules()
print(sum(rules.contains_gold(bag) for bag in rules.rules))
