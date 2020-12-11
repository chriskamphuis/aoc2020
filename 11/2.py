import numpy as np
from scipy.signal import convolve2d

seat_locations = []
for line in open('input.txt', 'r'):
    seat_locations.append([1 if x == 'L' else 0 for x in line.strip()])

seat_locations = np.array(seat_locations)
seats = np.zeros(seat_locations.shape)

def neighbour_locations(x, y):
    neighbours = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == dy == 0:
                continue
            dist = 1
            while True:
                if y+(dy*dist) < 0 or y+(dy*dist) >= seats.shape[0]:
                    break
                if x+(dx*dist) < 0 or x+(dx*dist) >= seats.shape[1]:
                    break
                if seat_locations[y+(dy*dist), x+(dx*dist)]:
                    neighbours.append([x+(dx*dist), y+(dy*dist)])
                    break
                else:
                    dist += 1
    return neighbours

def calculate_not_change(seats):
    not_change = np.zeros(seats.shape)
    for y in range(len(seats)):
        for x in range(len(seats[y])):
            neighbours = neighbour_locations(x, y)
            count = 0
            for x2, y2 in neighbours:
                if seats[y2, x2]:
                    count += 1  
            if count < 5:
                not_change[y, x] = 1
    return not_change

def calculate_to_occupy(seats):
    to_occupy = np.zeros(seats.shape)
    for y in range(len(seats)):
        for x in range(len(seats[y])):
            if seats[y, x]:
                continue
            neighbours = neighbour_locations(x, y)
            count = 0
            for x2, y2 in neighbours:
                if seats[y2, x2]:
                    count += 1 
            if count == 0:
                to_occupy[y, x] = 1
    return to_occupy

while True:
    not_change = calculate_not_change(seats) 
    to_occupy = calculate_to_occupy(seats) 
    to_occupy = np.multiply(to_occupy, seat_locations)
   
    new_seats = np.multiply(seats, not_change) 
    new_seats += to_occupy 

    
    if np.all(new_seats == seats):
        break

    seats = new_seats
print(int(np.sum(seats)))
