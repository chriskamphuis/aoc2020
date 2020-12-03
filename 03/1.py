trees = []
with open('input.txt', 'r') as f:
    for line in f:
        trees.append([True if v == '#' else False for v in line.strip()])

forest_length = len(trees[0])
x = y = 0
slope_x = 1
slope_y = 3
counter = 0
while x < len(trees):
    if trees[x][y]:
        counter+=1
    x += slope_x
    y = (y + slope_y) % forest_length
print(counter)
