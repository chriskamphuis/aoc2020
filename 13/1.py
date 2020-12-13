with open('input.txt') as f:
    startpoint = int(f.readline())
    busses = [bus for bus in f.readline().strip().split(',')]

lowest = float('inf')
first_bus = None
for bus in busses:
    if bus == 'x':
        continue
    bus = int(bus)
    waittime = bus-(startpoint+bus)%bus
    if  waittime < lowest:
        lowest = waittime
        first_bus = bus
print(first_bus*lowest)
