

fileObj =  open('../input/input3.txt', 'r')
lines = fileObj.read().splitlines()

rows = len(lines)
cols = len(lines[0])

print("rows: " , rows)
print("cols: " , cols)

cur_col = 0
count_trees = 0

for i in range(0, rows-1):
	cur_row = i+1
	cur_col = (cur_col + 3)%cols
	
	if lines[cur_row][cur_col] == '#':
		count_trees += 1

print(count_trees)



			
