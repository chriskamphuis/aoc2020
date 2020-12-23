class node:
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

puzzle_input = '123487596'
puzzle_input = [int(e) for e in puzzle_input]
maxi = max(puzzle_input) + 1

store = dict()

first = node(puzzle_input[0])
store[puzzle_input[0]] = first
prev = first
for p in puzzle_input[1:]:
    nxt = node(p)
    store[p] = nxt
    nxt.l = prev
    prev.r = nxt
    prev = nxt

while maxi != 1000000 + 1:
    nxt = node(maxi)
    store[maxi] = nxt
    nxt.l = prev
    prev.r = nxt
    prev = nxt
    maxi+=1

first.l = prev
prev.r = first
pivot = first

for _ in range(10000000):
    pickup = [pivot.r, pivot.r.r, pivot.r.r.r]
    new_connection = pivot.r.r.r.r 
    pivot.r = new_connection
    new_connection.l = pivot
    
    values_in_pickup = [p.v for p in pickup] 
    score = pivot.v - 1
    while score in values_in_pickup:
        score -= 1
    if score < 1:
        score = 1000000
        while score in values_in_pickup:
            score -= 1
    dest = store[score] 
    left = dest
    right = dest.r
    left.r = pickup[0]
    left.r.l = left
    right.l = pickup[-1]
    right.l.r = right
    pivot = pivot.r

pivot = store[1]
print(pivot.r.v * pivot.r.r.v)
