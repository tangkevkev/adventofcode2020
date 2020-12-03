

fileObj =  open('../input/input2.txt', 'r')
lines = fileObj.read().splitlines()
valid_count = 0

for line in lines:
	line_array = line.split(':')
	password = line_array[1]
	
	range_char_array = line_array[0].split(' ')
	range_array = range_char_array[0].split('-')
	
	first_index = int(range_array[0])-1
	second_index = int(range_array[1])-1

	password = password.replace(" ", "")
	char = range_char_array[1]
	char = char.replace(" ", "")

	cur_count = 0
	
	if password[first_index] == char:
		cur_count += 1
	
	if password[second_index] == char:
		cur_count += 1

	if cur_count == 1:
		valid_count += 1
	

print("valid count: " , valid_count)

			
