card, door = [int(e) for e in open('input.txt').read().strip().split('\n')]

# Card first
subject_number = 7
start = 1
loop_size = 1
while True:
    start *= subject_number
    start %= 20201227
    if start == card:
        break
    loop_size += 1

start = 1
for i in range(loop_size):
    start *= door
    start %= 20201227
print(start)
