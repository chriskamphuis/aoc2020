with open('input.txt', 'r') as f:
    numbers = {int(line) for line in f}
for n in list(numbers):
    if 2020 - n in numbers:
        print(n * (2020 - n))
        break
