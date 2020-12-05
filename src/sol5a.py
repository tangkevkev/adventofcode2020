

fileObj =  open('../input/input5.txt', 'r')
lines = fileObj.readlines()

max_seat = 0


for seat in lines:
    row_seat = seat[:7]
    col_seat = seat[7:10]


    row_binary = '0b'
    for elem in row_seat:
        row_binary += '0' if (elem == 'F') else '1'
    
    col_binary = '0b'
    for elem in col_seat:
        col_binary += '1' if (elem == 'R') else '0'
    
    col = int(col_binary,2)
    row = int(row_binary,2)

    seat_id = row*8+col
    max_seat = max(seat_id, max_seat)


print("Max seat: ", max_seat)