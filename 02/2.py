with open('input.txt', 'r') as f:
    valid = 0
    for line in f:
        count = 0
        possible, key, value = line.strip().split()
        minimum, maximum= [int(x) for x in possible.split('-')]
        key = key[0]
        if int(value[minimum-1] == key) + int(value[maximum-1] == key) == 1: 
            valid += 1
print(valid)
