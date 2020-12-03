with open('input.txt', 'r') as f:
    trees = [[1 if v == '#' else 0 for v in line.strip()] for line in f]

forest_length = len(trees[0])
x = y = 0
slope_y = 1
slope_x = 3
counter = 0
while y < len(trees):
    counter += trees[y][x]
    y += slope_y
    x = (x + slope_x) % forest_length
print(counter)
