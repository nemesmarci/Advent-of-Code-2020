from operator import itemgetter

from common import parse

allergen2ingredients = parse()[0]
allergen2ingredient = dict()

while any(len(x) > 0 for x in allergen2ingredients.values()):
    for allergen, ingredients in allergen2ingredients.items():
        if len(ingredients) == 1:
            ingredient = ingredients.pop()
            allergen2ingredient[allergen] = ingredient
            for other in allergen2ingredients:
                allergen2ingredients[other].discard(ingredient)

print(','.join(x[1] for x in sorted(allergen2ingredient.items(),
                                    key=itemgetter(0))))
