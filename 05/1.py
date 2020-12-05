with open('input.txt', 'r') as f:
    highest = -1
    for l in f:
        r = int(''.join(['0' if x == 'F' else '1' for x in l.strip()[:-3]]), 2)
        c = int(''.join(['0' if x == 'L' else '1' for x in l.strip()[-3:]]), 2)
        highest = r*8+c if r*8+c > highest else highest
print(highest)
