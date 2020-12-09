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
            seen.add(number)
            seen_in_order.append(number)
            break
    else:
        sol1 = number
        print(sol1)
        break

start = 0
end = 0
while True:
    value = 0
    end = start
    while value < sol1:
        value += seen_in_order[end]
        end += 1
    if value == sol1:
        break
    start += 1

contiguous = {x for x in seen_in_order[start:end]}
print(min(contiguous) + max(contiguous))
