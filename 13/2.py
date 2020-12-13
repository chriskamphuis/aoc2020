with open('input.txt') as f:
    startpoint = int(f.readline())
    busses = [bus for bus in f.readline().strip().split(',')]

offsets = sorted([[int(bus),i] for i, bus in enumerate(busses) if bus.isnumeric()])[::-1]
maximum_bus = 1
maximum_bus_offset = offsets[0][1]
while len(offsets) != 0:
    next_biggest_bus, next_offset = offsets.pop(0)
    while (startpoint + next_offset - maximum_bus_offset) % next_biggest_bus != 0:
        startpoint += maximum_bus
    maximum_bus *= next_biggest_bus
print(startpoint-maximum_bus_offset)
