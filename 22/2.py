p1, p2 = open('input.txt').read().split('\n\n')
p1 = [int(l) for l in p1.strip().split('\n') if l.isdigit()]
p2 = [int(l) for l in p2.strip().split('\n') if l.isdigit()]

f_score = lambda deck: sum([(i+1)*item for i, item in enumerate(deck[::-1])])

def recursive_combat(p1, p2):
    seen = set()
    while True:
        if ('p1'+','.join([str(e) for e in p1]) in seen or
            'p2'+','.join([str(e) for e in p2]) in seen):
            return 1, f_score(p1)
        seen.add('p1'+','.join([str(e) for e in p1]))
        seen.add('p2'+','.join([str(e) for e in p2]))
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if len(p1) >= c1 and len(p2) >= c2:
            winner, score = recursive_combat(p1[:c1].copy(), p2[:c2].copy())
        else:
            winner = 1 if c1 > c2 else 2
        if winner == 1:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
        if len(p1) == 0 or len(p2) == 0:
            winner = 1 if len(p1) > 0 else 2
            score = f_score(p1) if winner == 1 else f_score(p2)
            return winner, score

winner, score = recursive_combat(p1, p2)
print(score)
