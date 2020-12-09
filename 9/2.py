from common import parse, first_invalid


def find_sum(nums, target):
    for i in range(l := len(nums)):
        for j in range(i + 2, l):
            if (s := sum(lst := nums[i:j])) == target:
                return min(lst) + max(lst)
            elif s > target:
                break


print(find_sum(nums := parse(), first_invalid(nums)))
