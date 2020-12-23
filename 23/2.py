from common import Node, parse, run

cups = [Node(i) for i in parse()]
starting = cups[0]
rest = [Node(i) for i in range(10, 1000000 + 1)]

for i, cup in enumerate(cups):
    cup.next = cups[i + 1] if i != len(cups) - 1 else rest[0]

for i, cup in enumerate(rest):
    cup.next = rest[i + 1] if i != len(rest) - 1 else cups[0]

cups = sorted(cups, key=lambda cup: cup.value) + rest

run(cups, starting, 10000000)

print(cups[0].next.value * cups[0].next.next.value)
