trees = []
with open('input.txt', 'r') as f:
    for line in f:
        trees.append([True if v == '#' else False for v in line.strip()])

forest_length = len(trees[0])

counts = 1

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for slope_y, slope_x in slopes:
    x = y = 0 
    counter = 0
    while x < len(trees):
        if trees[x][y]:
            counter+=1
        x += slope_x
        y = (y + slope_y) % forest_length
    counts *= counter
print(counts)
