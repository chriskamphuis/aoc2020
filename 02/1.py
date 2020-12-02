with open('input.txt', 'r') as f:
    valid = 0
    for line in f:
        count = 0
        possible, key, value = line.strip().split()
        minimum, maximum= [int(x) for x in possible.split('-')]
        key = key[0]
        for letter in value:
            if key == letter: 
                count += 1
        if minimum <= count <= maximum:
            valid += 1
print(valid)
