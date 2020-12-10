numbers = {int(i) for i in open('input.txt')}
pivot = 0
jumps = [0, 0, 1]
ordered = []
while numbers:
    ordered.append(pivot)
    for value in [1, 2, 3]:
        if pivot+value in numbers:
            numbers.remove(pivot+value)
            jumps[value-1] += 1
            pivot += value
            break
print(jumps[0]*jumps[2])
