numbers = (int(n.strip()) for n in open('input.txt', 'r').readlines())
seen = set()
seen_in_order = list()
preamble = 25

for i in range(preamble):
    number = next(numbers)
    seen.add(number)
    seen_in_order.append(number)

while True:
    number = next(numbers)
    for n in seen:
        if number - n in seen:
            to_remove = seen_in_order[-25]
            seen.remove(to_remove)
            seen.add(number)
            seen_in_order.append(number)
            break
    else:
        sol1 = number
        print(sol1)
        break

start = 0
end = 0
score = seen_in_order[0]
while score != sol1:
    if score < sol1:
        end += 1
        score += seen_in_order[end]
    if score > sol1:
        score -= seen_in_order[start]
        start += 1

contiguous = {x for x in seen_in_order[start:end]}
print(min(contiguous) + max(contiguous))
