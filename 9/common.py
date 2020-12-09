from itertools import combinations


def parse():
    with open('input.txt') as data:
        return list(map(int, data))


def first_invalid(nums):
    return next(nums[i] for i in range(25, len(nums))
                if not any(sum(pair) == nums[i]
                           for pair in combinations(nums[i - 25: i], 2)))
