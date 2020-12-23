fileObj =  open('../input/input11.txt', 'r')
seats = fileObj.read().splitlines()
seats = [list(s) for s in seats]

rows = len(seats)
cols = len(seats[0])

offset = [(i,j) for i in [-1,0,1] for j in [-1,0,1] if not (i == 0 and j == 0)]
all_seats = [(i,j) for i in range(rows) for j in range(cols)]


new_seats = seats[:]

while(True):
    for (i,j) in all_seats:
        adj_seats = [(i+s, j+t) for (s,t) in offset if i+s >= 0 and i+s < rows and j+t >= 0 and j+t < cols]
        count_occupied = [seats[x][y] for (x,y) in adj_seats].count('#')
        if seats[i][j] == 'L' and count_occupied == 0:
            new_seats[i] = new_seats[i][0:j] + ['#'] + new_seats[i][j+1:]
        elif seats[i][j] == '#' and count_occupied >= 4:
            new_seats[i] = new_seats[i][0:j] + ['L'] + new_seats[i][j+1:]
    if seats == new_seats:
        break
    seats = new_seats[:]

all_occupied_seat = [seats[i][j] for (i,j) in all_seats].count('#')
print(all_occupied_seat)
