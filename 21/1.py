from common import parse

appeared, dangerous = parse()[1:]

print(sum(count for ingredient, count in appeared.items()
          if ingredient not in dangerous))
