count = 0
with open('input.txt') as f:
    group = set()
    for line in f: 
        if not line.strip():
            count += len(group)
            group = set()
            continue
        group |= set(line.strip())
    count += len(group)
print(count)
