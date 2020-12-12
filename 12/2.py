from common import instructions, manhattan

ship = [0, 0]
waypoint = [1, 10]

for action, num in instructions():
    if action == 'R':
        for _ in range(num % 360 // 90):
            waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
    elif action == 'L':
        for _ in range(num % 360 // 90):
            waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
    elif action == 'N':
        waypoint[0] += num
    elif action == 'E':
        waypoint[1] += num
    elif action == 'S':
        waypoint[0] -= num
    elif action == 'W':
        waypoint[1] -= num
    elif action == 'F':
        ship[0] += num * waypoint[0]
        ship[1] += num * waypoint[1]

print(manhattan(ship))
