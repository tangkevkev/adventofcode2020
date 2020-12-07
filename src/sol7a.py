fileObj =  open('../input/input7.txt', 'r')
lines = fileObj.read().splitlines()
target_color = 'shiny gold'


#Mapping the bags containing other colored bags
color_mapping = dict()
for line in lines:
	line_array = line.split(' ')
	color = line_array[0] + ' ' + line_array[1]
	if line_array[-3] == 'no':
		color_mapping[color] = []
		continue
	
	number_of_color = int((len(line_array)-4)/4)
	cur_mapping = []

	for i in range(0, number_of_color):
		cur_color = line_array[(i+1)*4 + 1] + ' ' + line_array[(i+1)*4 + 2]
		cur_mapping.append(cur_color)
	
	color_mapping[color] = cur_mapping


count_result = 0

for color in color_mapping:
	if color == target_color:
		continue
	visited_colors = set()
	visited_colors.add(color)
	toDo = [color]

	break_loop = False
	while len(toDo) > 0:
		cur_color = toDo.pop(0)
		for vis_color in color_mapping[cur_color]:
			if vis_color == target_color:
				count_result += 1
				break_loop = True
				break
			if vis_color not in visited_colors:
				visited_colors.add(vis_color)
				toDo.append(vis_color)
		if break_loop:
			break

print(count_result)


	
	


			
