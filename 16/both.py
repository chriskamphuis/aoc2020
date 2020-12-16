from collections import defaultdict
from pprint import pprint 
ranges = []
your_ticket = []
other_tickets = []
range_to_name = dict()
name_to_ranges = defaultdict(list)

with open('input.txt', 'r') as f:
    while True: 
        line = f.readline().strip()
        if len(line) == 0:
            break
        name, line = line.split(':')
        line = line.split(' ')
        for idx in [-3, -1]:
            bounds = [int(e) for e in line[idx].split('-')]
            rng = range(bounds[0], bounds[1]+1)
            range_to_name[rng] = name
            ranges.append(rng)
            name_to_ranges[name].append(rng)
    f.readline()
    your_ticket = [int(e) for e in f.readline().strip().split(',')]
    f.readline(); f.readline()
    for line in f.readlines():
        other_tickets.append([int(e) for e in line.strip().split(',')])


new_other_tickets = []
error_rate = 0
for ticket in other_tickets:
    old_error = error_rate
    for value in ticket:
        if not any([value in c for c in ranges]):
            error_rate += value
    if old_error == error_rate:
        new_other_tickets.append(ticket)

print(f'Part 1: {error_rate}')
other_tickets = new_other_tickets
names = name_to_ranges.keys()

index_to_valid_map = dict()
for i in range(len(other_tickets[0])):
    valid_names = names
    for ticket in other_tickets: 
        valid_ranges = [rng for rng in ranges if ticket[i] in rng]
        valid_fields = {range_to_name[rng] for rng in valid_ranges}
        valid_names = {name for name in valid_names if name in valid_fields}
    index_to_valid_map[i] = valid_names

name_index_map = defaultdict(list)
for index, names in index_to_valid_map.items():
    for name in names:
        name_index_map[name].append(index)

small_first = sorted([[k,v] for k,v in name_index_map.items()], key=lambda x: len(x[1]))

combinations = [[]]
for possible in small_first:
    new_combi = []
    for idx in possible[1]:
        for c in combinations:
            if idx not in c:
                new_combi.append(c + [idx])
    combinations = new_combi
names = [e[0] for e in small_first]

final = [combi for name, combi in zip(names, combinations[0]) if name.startswith('departure')]
product = 1
for v in final:
    product *= your_ticket[v]
print(f'Part 2: {product}')
