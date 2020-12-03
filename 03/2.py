with open('input.txt', 'r') as f:
    trees = [[1 if v == '#' else 0 for v in line.strip()] for line in f]

forest_length = len(trees[0])
counts = 1
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

for slope_x, slope_y in slopes:
    x = y = 0 
    counter = 0
    while y < len(trees):
        counter+=trees[y][x]
        y += slope_y
        x = (x + slope_x) % forest_length
    counts *= counter
print(counts)
