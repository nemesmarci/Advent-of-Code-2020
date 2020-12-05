from common import seat_id

with open('input.txt') as data:
    ids = [seat_id(line) for line in data]
    print(sum(range(max(ids) + 1)) - sum(range(min(ids))) - sum(ids))
