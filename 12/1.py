from common import instructions, manhattan

facing = 90
pos = [0, 0]

for action, num in instructions():
    if action == 'R':
        facing += num
        facing %= 360
    elif action == 'L':
        facing -= num
        facing %= 360
    elif action == 'N' or action == 'F' and facing == 0:
        pos[0] += num
    elif action == 'E' or action == 'F' and facing == 90:
        pos[1] += num
    elif action == 'S' or action == 'F' and facing == 180:
        pos[0] -= num
    elif action == 'W' or action == 'F' and facing == 270:
        pos[1] -= num


print(manhattan(pos))
