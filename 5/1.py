from common import seat_id

with open('input.txt') as data:
    print(max(map(seat_id, data)))
