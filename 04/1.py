man_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
passports = []
with open('input.txt', 'r') as f:
    passport = dict()
    for line in f:
        if len(line.strip()) == 0:
            passports.append(passport)
            passport = dict()
            continue
        for x in line.strip().split(' '):
            k,v = x.split(':')
            passport[k] = v
    passports.append(passport)
valid = 0
for p in passports:
    if len(set(p.keys()).intersection(man_fields)) == 7:
        valid += 1
print(valid)
