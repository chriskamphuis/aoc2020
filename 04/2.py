import re

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
    if not(len(set(p.keys()).intersection(man_fields)) == 7):
        continue
    if not(1920 <= int(p['byr']) <= 2002):
        continue
    if not(2010 <= int(p['iyr']) <= 2020):
        continue
    if not(2020 <= int(p['eyr']) <= 2030):
        continue
    if not(p['hgt'][-2:] == 'cm' and 150 <= int(p['hgt'][:-2]) <= 193 or
           p['hgt'][-2:] == 'in' and 59 <= int(p['hgt'][:-2]) <= 76):
        continue
    if not(re.match(r'#[0-9a-f]{6}', p['hcl']) and len(p['hcl']) == 7):
        continue
    if not(p['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}):
        continue
    if not(re.match(r'[0-9]{9}', p['pid']) and len(p['pid']) == 9):
        continue
    valid += 1
print(valid)
