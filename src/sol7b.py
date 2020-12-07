def recursion(cur_color, color_count_map, color_mapping):	
	if cur_color in color_count_map:
		return color_count_map[cur_color]
	
	if len(color_mapping[cur_color]) == 0:
		return 1
	#Don't forget to count the initial bag	
	total = 1
	for entry in color_mapping[cur_color]:
		(color, count) = (entry[0], entry[1])
		total += count*recursion(color, color_count_map, color_mapping)
	color_count_map[cur_color] = total
	return total



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
		cur_count = int(line_array[ (i+1)*4])
		cur_mapping.append((cur_color, cur_count))
	color_mapping[color] = cur_mapping


color_count_map = dict()
result = recursion(target_color, color_count_map, color_mapping)

print(result-1)
	






	
	


			
