numbers = {int(i) for i in open('input.txt')}
numbers_paths_map = {n:0 for n in numbers}

last = pivot = 0
ordered = []
numbers_paths_map[0] = 1

while numbers:
    ordered.append(pivot)
    for value in [1, 2, 3]:
        if pivot+value in numbers:
            numbers.remove(pivot+value)
            pivot += value
            break

for i, value in enumerate(ordered):
    for j in [1, 2, 3]:
        if value+j in numbers_paths_map.keys():
            numbers_paths_map[value+j] += numbers_paths_map[ordered[i]]
            last = numbers_paths_map[value+j] 

print(last)
