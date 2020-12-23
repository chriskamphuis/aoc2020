class node:
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

puzzle_input = '123487596'
puzzle_input = [int(e) for e in puzzle_input]

first = node(puzzle_input[0])
prev = first
for p in puzzle_input[1:]:
    nxt = node(p)
    nxt.l = prev
    prev.r = nxt
    prev = nxt
first.l = prev
prev.r = first
pivot = first

for _ in range(100):
    pickup = [pivot.r, pivot.r.r, pivot.r.r.r]
    new_connection = pivot.r.r.r.r 
    pivot.r = new_connection
    new_connection.l = pivot
    dest_v, dest = -1, None
    i = pivot.r
    while i.v != pivot.v:
        if i.v < pivot.v and i.v > dest_v:
            dest_v = i.v
            dest = i
        i = i.r
    if dest is None:
        dest_v, dest = -1, None
        i = pivot.r
        while i.v != pivot.v:
            if i.v > dest_v:
                dest_v = i.v
                dest = i
            i = i.r
    left = dest
    right = dest.r
    left.r = pickup[0]
    left.r.l = left
    right.l = pickup[-1]
    right.l.r = right
    pivot = pivot.r

while True:
    if pivot.v == 1:
        break
    pivot = pivot.r
output = []
for _ in range(len(puzzle_input)-1):
    pivot = pivot.r
    output.append(str(pivot.v))
print(''.join(output))

