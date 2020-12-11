import numpy as np
from scipy.signal import convolve2d

seat_locations = []
for line in open('input.txt', 'r'):
    seat_locations.append([1 if x == 'L' else 0 for x in line.strip()])

seat_locations = np.array(seat_locations)
seats = np.zeros(seat_locations.shape)

neighbours = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
full = [[1, 1, 1,], [1, 1, 1], [1, 1, 1]]

while True:
    not_change = (convolve2d(seats, neighbours, 'same') < 4).astype(np.int)
    
    to_occupy = (convolve2d(seats, full, 'same') == 0).astype(np.int)
    to_occupy = np.multiply(to_occupy, seat_locations)
   
    new_seats = np.multiply(seats, not_change) 
    new_seats += to_occupy 
    
    if np.all(new_seats == seats):
        break

    seats = new_seats
print(int(np.sum(seats)))
