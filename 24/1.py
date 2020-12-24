import re, operator

def update_location(tile, match):
    if match == 'e': direction = (2, 0)
    if match == 'se': direction = (1, -1)
    if match == 'sw': direction = (-1, -1)
    if match == 'w': direction = (-2, 0)
    if match == 'nw': direction = (-1, 1)
    if match == 'ne': direction = (1, 1)
    return tuple(map(operator.add, tile, direction))

flipped = set()

tiles = [line for line in open('input.txt').read().strip().split('\n')]
for tile in tiles:
    loc = (0, 0)
    matches = re.findall(r'(e|se|sw|w|nw|ne)', tile)
    for match in matches:
        loc = update_location(loc, match)
    if loc not in flipped:
        flipped.add(loc)
    else:
        flipped.remove(loc)
print(len(flipped))
