passes = set()
with open('input.txt', 'r') as f:
    for l in f:
        r = int(''.join(['0' if x == 'F' else '1' for x in l.strip()[:-3]]), 2)
        c = int(''.join(['0' if x == 'L' else '1' for x in l.strip()[-3:]]), 2)
        passes.add(r*8+c)
for value in passes:
    if value+1 not in passes and value+2 in passes:
        print(value+1)
        break
