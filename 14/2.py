from collections import defaultdict

memory = defaultdict(int)
mask = ['X'] * 36

def find_combinations(address):
    addresses = []
    cnt = 0
    idx = []
    for i in range(len(address)):
        if address[i] == 'X':
            cnt += 1
            idx.append(i)
    combinations = 2**cnt
    for i in range(combinations):
        bitstring = bin(i)[2:]
        tmp_address = [e for e in address]
        for i, bit in enumerate(bitstring[::-1]):
            j = idx[-(i+1)]
            tmp_address[j] = bit
        tmp_address = [e for e in ''.join(tmp_address).replace('X', '0')]
        addresses.append(tmp_address)
    return addresses

with open('input.txt', 'r') as f:
    for line in f:
        operation, value = line.strip().split(' = ')
        if operation == 'mask': 
            mask = [x for x in value]
        else: 
            address = int(operation[4:-1])
            addresses = [e for e in mask]
            b_value = bin(int(address))[2:]
            for i, bit in enumerate(b_value[::-1]):
                if mask[-(i+1)] == 'X':
                    addresses[-(i+1)] = 'X'
                elif mask[-(i+1)] == '1':
                    addresses[-(i+1)] = '1'
                else:
                    addresses[-(i+1)] = bit
            for i in range(len(b_value), 36):
                if mask[-(i+1)] == 'X':
                    addresses[-(i+1)] = 'X'
                elif mask[-(i+1)] == '1':
                    addresses[-(i+1)] = '1'
                else:
                    addresses[-(i+1)] = '0'
            combinations = [int(''.join(e), 2) for e in find_combinations(addresses)]
            for c in combinations:
                memory[c] = int(value)

print(sum([v for _, v in memory.items()]))
