from pprint import pprint
from collections import defaultdict
import numpy as np
import sys

tiles = open('input.txt', 'r').read().strip().split('\n\n')
size = len(tiles[1].split('\n')[1])
tiles = {int(t[0][5:-1]):np.array([[int(e) for e 
         in x.replace('#', '1').replace('.', '0')]
         for x in t[1:]]) for t in [tile.split('\n') for tile in tiles]}
keys = tiles.keys()
border_to_key_map = defaultdict(list)

for k in keys:
    sides = []
    tile = tiles[k]
    for start in [0, size-1]:
        tmp = [str(e) for e in tile[start,:]]
        border_to_key_map[''.join(tmp)].append(k)
        border_to_key_map[''.join(tmp[::-1])].append(k)

        tmp = [str(e) for e in tile[:,start]]
        border_to_key_map[''.join(tmp)].append(k)
        border_to_key_map[''.join(tmp[::-1])].append(k)

counter = defaultdict(int)
outsides = set()
for k, v in border_to_key_map.items():
    if len(v) == 1:
        counter[v[0]] += 1
        outsides.add(k)

corners = []
prod = 1
for k, v in counter.items():
    if v == 4:
        prod *= k
        corners.append(k)
# p1
print(prod)

first_corner = corners[0]

todo = set(keys)
todo.remove(first_corner)

puzzle = [[None for j in range(12)] for i in range(12)]

for y in range(12):
    for x in range(12):
        if x == 0 == y:
            part = tiles[first_corner]
            while (''.join([str(e) for e in part[:,0]]) not in outsides 
                   or ''.join([str(e) for e in part[0,:]]) not in outsides):
                part = np.rot90(part)
            puzzle[y][x] = part
        elif x != 0:
            last_piece = puzzle[y][x-1]
            right_border = ''.join([str(e) for e in last_piece[:,-1]])
            nxt = [e for e in border_to_key_map[right_border] if e in todo][0]
            todo.remove(nxt)
            tile = tiles[nxt]
            nxt_tile = None
            for _ in range(4):
                if right_border == ''.join([str(e) for e in tile[:,0]]):
                    nxt_tile = tile
                else:
                    tile = np.rot90(tile)
            tile = np.fliplr(tile)
            for _ in range(4):
                if right_border == ''.join([str(e) for e in tile[:,0]]):
                    nxt_tile = tile
                else:
                    tile = np.rot90(tile)
            puzzle[y][x] = nxt_tile
        else:
            last_piece = puzzle[y-1][x]
            bot_border = ''.join([str(e) for e in last_piece[-1,:]])
            nxt = [e for e in border_to_key_map[bot_border] if e in todo][0]
            todo.remove(nxt)
            tile = tiles[nxt]
            nxt_tile = None
            for _ in range(4):
                if bot_border == ''.join([str(e) for e in tile[0,:]]):
                    nxt_tile = tile
                else:
                    tile = np.rot90(tile)
            tile = np.fliplr(tile)
            for _ in range(4):
                if bot_border == ''.join([str(e) for e in tile[0,:]]):
                    nxt_tile = tile
                else:
                    tile = np.rot90(tile)
            puzzle[y][x] = nxt_tile

rows = []
for p in puzzle:
    row = [part[1:-1,1:-1] for part in p]
    start = row[0] 
    for e in row[1:]:
        start = np.hstack((start, e))
    rows.append(start)

start = rows[0]
for row in rows[1:]:
    start = np.vstack((start, row))

full_puzzle = start
monster = ['                  # ',
           '#    ##    ##    ###', 
           ' #  #  #  #  #  #   ']
for i in range(len(monster)):
    row = monster[i]
    row = [1 if r == '#' else 0 for r in row]
    monster[i] = row

monster = np.array(monster)

height = len(monster)
width = len(monster[0])
mask = np.zeros(full_puzzle.shape)

for _ in range(4):
    full_puzzle = np.rot90(full_puzzle)
    mask = np.rot90(mask)
    for x in range(full_puzzle.shape[0] - width):
        for y in range(full_puzzle.shape[0] - height):
            count = 0
            for dy, row in enumerate(monster):
                for dx, v in enumerate(row):
                    if v == 1 == full_puzzle[y+dy, x+dx]:
                        count+=1
            if count == 15:
                for dy, row in enumerate(monster):
                    for dx, v in enumerate(row):
                        if v == 1 == full_puzzle[y+dy, x+dx]:
                            mask[y+dy, x+dx] = 1


full_puzzle = np.fliplr(full_puzzle)
mask = np.fliplr(mask)

for _ in range(4):
    full_puzzle = np.rot90(full_puzzle)
    mask = np.rot90(mask)
    for x in range(full_puzzle.shape[0] - width):
        for y in range(full_puzzle.shape[0] - height):
            count = 0
            for dy, row in enumerate(monster):
                for dx, v in enumerate(row):
                    if v == 1 == full_puzzle[y+dy, x+dx]:
                        count+=1
            if count == 15:
                for dy, row in enumerate(monster):
                    for dx, v in enumerate(row):
                        if v == 1 == full_puzzle[y+dy, x+dx]:
                            mask[y+dy, x+dx] = 1

print(int(np.sum(full_puzzle) - np.sum(mask)))
