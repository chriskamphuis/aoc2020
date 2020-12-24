import re, operator

dirs = [(2, 0), (1, -1), (-1, -1), (-2, 0), (-1, 1), (1, 1)]

def update_location(tile, match):
    if match == 'e': direction = (2, 0)
    if match == 'se': direction = (1, -1)
    if match == 'sw': direction = (-1, -1)
    if match == 'w': direction = (-2, 0)
    if match == 'nw': direction = (-1, 1)
    if match == 'ne': direction = (1, 1)
    return tuple(map(operator.add, tile, direction))

neighbours = lambda tile: [tuple(map(operator.add, tile, d)) for d in dirs]
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

for day in range(100):
    if day % 10 == 0:
        print(day)
    black_to_white = set()
    white_to_consider = set()
    white_to_black = set()
    for tile in flipped:
        neighs = neighbours(tile)
        cnt = sum([int(n in flipped) for n in neighs])
        if cnt == 0 or cnt > 2:
            black_to_white.add(tile)
        for n in neighs:
            if n not in flipped:
                white_to_consider.add(n)
        for t in white_to_consider:
            if sum([int(n in flipped) for n in neighbours(t)]) == 2:
                white_to_black.add(t)
    for t in black_to_white:
        flipped.remove(t)
    for t in white_to_black:
        flipped.add(t)
print(len(flipped))
