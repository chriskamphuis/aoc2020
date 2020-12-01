numbers = set()
with open('input.txt', 'r') as f:
    for line in f: 
        n = int(line)
        if 2020 - n in numbers:
            print(n*(2020 - n))
            break
        else:
            numbers |= {n}
