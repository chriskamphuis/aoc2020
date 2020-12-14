from collections import defaultdict

memory = defaultdict(list)
mask = ['X'] * 36

with open('input.txt', 'r') as f:
    for line in f:
        operation, value = line.strip().split(' = ')
        if operation == 'mask': 
            mask = [x for x in value]
        else: 
            address = int(operation[4:-1])
            memory[address] = [e for e in mask]
            b_value = bin(int(value))[2:]
            for i, bit in enumerate(b_value[::-1]):
                if mask[-(i+1)] == 'X':
                    memory[address][-(i+1)] = int(bit)
                else:
                    memory[address][-(i+1)] = int(mask[-(i+1)])
            for i in range(len(b_value), 36):
                if mask[-(i+1)] == 'X':
                    memory[address][-(i+1)] = 0
                else:
                    memory[address][-(i+1)] = int(mask[-(i+1)])

print(sum([int(''.join([str(x) for x in v]), 2) for _, v in memory.items()]))
