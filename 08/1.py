instructions = []
with open('input.txt', 'r') as f:
    for line in f:
        instruction, value = line.strip().split(' ')
        instructions.append([instruction, int(value)])
pos = accumulator = 0
order = 1
visited = dict()
while pos not in visited.keys():
    visited[pos] = order
    inst = instructions[pos]
    if inst[0] == 'acc':
        accumulator += inst[1]
        pos += 1
    elif inst[0] == 'jmp':
        pos += inst[1]
    else:
        pos += 1
print(accumulator)
