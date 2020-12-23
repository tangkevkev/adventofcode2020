fileObj =  open('../input/input11.txt', 'r')
seats = fileObj.read().splitlines()
seats = [list(s) for s in seats]

rows = len(seats)
cols = len(seats[0])


all_seats = [(i,j) for i in range(rows) for j in range(cols)]
all_directions = []
all_directions += [[(0,i) for i in range(1, cols)]]
all_directions += [[(0,-i) for i in range(1, cols)]]
all_directions += [[(i, 0) for i in range(1, rows)]]
all_directions += [[(-i, 0) for i in range(1, rows)]]
all_directions += [[(i, i) for i in range(1, min(rows,cols))]]
all_directions += [[(i, -i) for i in range(1, min(rows,cols))]]
all_directions += [[(-i, i) for i in range(1, min(rows,cols))]]
all_directions += [[(-i, -i) for i in range(1, min(rows,cols))]]


new_seats = seats[:]

while(True):

    for (i,j) in all_seats:
        #check for each direction the state of the seats
        count_occupied = 0        

        for cur_direction in all_directions:
            for (s,t) in cur_direction:
                if i+s >= 0 and i+s < rows and j+t >= 0 and j+t < cols:
                    if seats[i+s][j+t] == '#':
                        count_occupied += 1
                        break
                    elif seats[i+s][j+t] == 'L':
                        break
                else:
                    break
        
        if seats[i][j] == 'L' and count_occupied == 0:
            new_seats[i] = new_seats[i][0:j] + ['#'] + new_seats[i][j+1:]
        elif seats[i][j] == '#' and count_occupied >= 5:
            new_seats[i] = new_seats[i][0:j] + ['L'] + new_seats[i][j+1:]
    

    if seats == new_seats:
        break
    seats = new_seats[:]
    

all_occupied_seat = [seats[i][j] for (i,j) in all_seats].count('#')
print(all_occupied_seat)
