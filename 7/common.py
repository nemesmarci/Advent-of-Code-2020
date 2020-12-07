import re


class Rules:
    def __init__(self):
        bag_regex = re.compile(r'((\d+ )?(\w+ \w+) bag(?:s)?)')
        self.rules = dict()
        with open('input.txt') as data:
            for line in map(str.strip, data):
                matches = re.findall(bag_regex, line)
                bag = matches[0][2]
                self.rules[bag] = {other: num for _, num, other in matches[1:]}

    def contains_gold(self, bag):
        if 'no other' in self.rules[bag]:
            return False
        return 'shiny gold' in self.rules[bag] or \
            any(map(self.contains_gold, self.rules[bag]))

    def count_bags(self, bag):
        if 'no other' in self.rules[bag]:
            return 0
        return sum(int(self.rules[bag][other]) * (self.count_bags(other) + 1)
                   for other in self.rules[bag])
