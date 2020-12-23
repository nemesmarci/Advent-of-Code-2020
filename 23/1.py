from common import Node, parse, run

cups = [Node(i) for i in parse()]
starting = cups[0]

for i, cup in enumerate(cups):
    cup.next = cups[i + 1] if i != len(cups) - 1 else cups[0]

cups = sorted(cups, key=lambda cup: cup.value)

run(cups, starting, 100)

current = cups[0].next
order = []
while current.value != 1:
    order.append(current.value)
    current = current.next
print(''.join(str(i) for i in order))
