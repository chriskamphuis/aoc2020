for f in [set.union, set.intersection]:
    print(sum([len(f(*[set(x) for x in l.split('\n')])) for l in open('input.txt').read().split('\n\n')]))
