def solve(target):
    with open('input.txt') as data:
        nums = map(int, data.readline().split(','))

    spoken = {num: i + 1 for i, num in enumerate(nums)}
    curr = 0

    for i in range(len(spoken) + 1, target):
        n = spoken.get(curr, i)
        spoken[curr] = i
        curr = i - n
    return curr
