puzzle_input = [0,14,6,20,1,4]

numbers = [2020, 30000000]

number_lsm = {e:i+1 for i, e in enumerate(puzzle_input)}
previous_value = puzzle_input[-1]
i = len(puzzle_input)+1

first_time = True
for n in numbers: 
    while True:
        if first_time:
            next_number = 0
        else:
            next_number = (i-1) - number_lsm[previous_value]
        number_lsm[previous_value] = i-1
        first_time = next_number not in number_lsm.keys()
        previous_value = next_number 
        i+=1
        if i == n+1: 
            print(f'{next_number}')
            break
