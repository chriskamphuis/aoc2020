directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
direction_map = {d:i for d, i in zip('ESWN', directions)}
direction_index = 0
loc = [0, 0]

for line in open('input.txt'):
    action = line[0]
    value = int(line[1:])
    if action == 'F':
        loc = [loc[i] + directions[direction_index][i] * value for i in [0, 1]]
    if action in 'ESWN':
        direction = direction_map[action]
        loc = [loc[i] + direction[i] * value for i in [0, 1]]
    if action == 'L':
        value = -value + 360
        action = 'R'
    if action == 'R':
        direction_index = (direction_index + (value//90)) % 4
print(sum([abs(x) for x in loc]))
