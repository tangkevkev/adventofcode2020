

fileObj =  open('../input/input3.txt', 'r')
lines = fileObj.read().splitlines()

rows = len(lines)
cols = len(lines[0])

print("rows: " , rows)
print("cols: " , cols)



multiplied_tree = 1

traverse_orders = [(1,1), (3,1), (5,1), (7,1), (1,2)]

for order in traverse_orders:
	cur_row = 0
	cur_col = 0
	
	right = order[0]
	down = order[1]
	
	count_trees = 0
    
	
	while cur_row < rows-1:
	    cur_row += down
	    cur_col = (cur_col + right)%cols
       
	    if lines[cur_row][cur_col] == '#':
		    count_trees += 1
              
	multiplied_tree *= count_trees
    


print(multiplied_tree)

