from math import prod

from common import parse, is_corner

print(prod(int(name) for name, tile in parse().items() if is_corner(tile)))
