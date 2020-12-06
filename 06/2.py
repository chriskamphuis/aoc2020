count = 0
with open('input.txt') as f:
    group = None
    for line in f:
        if line.strip() and group is None:
            group = set(line.strip())
            continue
        if not line.strip():
            count += len(group)
            group = None
            continue
        group &= set(line.strip())
    count += len(group)
print(count)
