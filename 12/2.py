import numpy as np

waypoint = [10, 1] # 'EN' (west and south are negative)
directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
direction_map = {d:i for d, i in zip('ESWN', directions)}
loc = [0, 0]


for line in open('input.txt'):
    action = line[0]
    value = int(line[1:])
    if action == 'F':
        loc = [loc[i] + waypoint[i] * value for i in [0, 1]]
    if action in 'ESWN':
        direction = direction_map[action]
        waypoint = [waypoint[i] + direction[i] * value for i in [0, 1]]
    if action == 'L':
        value = -value + 360
        action = 'R'
    if action == 'R':
        for _ in range(value//90):
            waypoint = np.array(waypoint) @ np.array([[0, -1], [1, 0]])
            waypoint = list(waypoint)
print(sum([abs(x) for x in loc]))
