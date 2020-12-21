from collections import defaultdict, Counter
from functools import reduce


def parse():
    allergen2ingredients = defaultdict(list)
    appeared = Counter()
    with open('input.txt') as data:
        for line in data:
            ingredients, allergens = line.strip().split(' (contains ')
            ingredients = ingredients.split()
            appeared += Counter(ingredients)
            allergens = allergens.strip(')').split(', ')
            for allergen in allergens:
                allergen2ingredients[allergen].append(set(ingredients))

    dangerous = set()
    for allergen, ingredients in allergen2ingredients.items():
        common = reduce(set.intersection, ingredients)
        dangerous |= common
        allergen2ingredients[allergen] = common

    return allergen2ingredients, appeared, dangerous
