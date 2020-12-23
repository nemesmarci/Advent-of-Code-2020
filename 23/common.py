class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def parse():
    with open('input.txt') as data:
        return [int(c) for c in data.read()]


def get_target(current, picked, size):
    target = current - 1
    if target == 0:
        target = size
    while target in picked:
        target -= 1
        if target == 0:
            target = size
    return target - 1


def run(cups, current, rounds):
    size = len(cups)
    for i in range(rounds):
        moved1 = current.next
        moved2 = moved1.next
        moved3 = moved2.next
        new_next = moved3.next
        current.next = new_next
        target_cup = cups[
            get_target(current.value,
                       [moved1.value, moved2.value, moved3.value],
                       size)]
        old_next = target_cup.next
        target_cup.next = moved1
        moved3.next = old_next
        current = current.next
