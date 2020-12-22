p1, p2 = open('input.txt').read().split('\n\n')
p1 = [int(l) for l in p1.strip().split('\n') if l.isdigit()]
p2 = [int(l) for l in p2.strip().split('\n') if l.isdigit()]

while True:
    c1 = p1.pop(0)
    c2 = p2.pop(0)
    if c1 > c2:
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c2)
        p2.append(c1)
    if len(p1) == 0 or len(p2) == 0:
        break
final = p1 if len(p2) == 0 else p2
print(sum([(i+1)*item for i, item in enumerate(final[::-1])]))
