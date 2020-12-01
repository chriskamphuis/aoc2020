import sys
with open('input.txt', 'r') as f:
    numbers = {int(line) for line in f}
for n in list(numbers):
    for k in list(numbers):
        if 2020 - n - k in numbers:
            print(n * (2020 - n - k) * k)
            sys.exit()
