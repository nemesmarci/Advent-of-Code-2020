from itertools import count

with open('input.txt') as data:
    card_pub, door_pub = map(int, data.read().split('\n')[:-1])

card_loop = next(loop for loop in count(1)
                 if pow(7, loop, 20201227) == card_pub)

print(pow(door_pub, card_loop, 20201227))
