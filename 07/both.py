from collections import defaultdict 

forward_map = dict()
backward_map = defaultdict(list)

with open('input.txt', 'r') as f:
    for line in f:
        key, values = line.strip().split(' contain ')
        key = key[:-4] 
        values = values[:-1]
        values = [' '.join(v.split(' ')[:-1]) for v in values.split(', ')]
        values = {v[2:].strip() : int(v[0]) for v in values if v != 'no other'}
        forward_map[key.strip()] = values
        for k, v in values.items():
            backward_map[k.strip()].append(key.strip())

seen = set()
to_consider = {'shiny gold'}
while to_consider:
    value = to_consider.pop()
    seen.add(value)
    for v in backward_map[value]:
        if v not in seen:
            to_consider.add(v)
# part 1
print(len(seen)-1)

# part 2
def needed(bag):
    needed_bags = 0
    for new_bag, count in forward_map[bag].items():
        needed_bags += count * needed(new_bag) + count
    return needed_bags

print(needed('shiny gold'))
