

fileObj =  open('../input/input2.txt', 'r')
lines = fileObj.read().splitlines()
valid_count = 0

for line in lines:
	line_array = line.split(':')
	password = line_array[1]
	
	range_char_array = line_array[0].split(' ')
	range_array = range_char_array[0].split('-')
	
	lower_bound = int(range_array[0])
	upper_bound = int(range_array[1])
	char = range_char_array[1]
	char = char.replace(" ", "")
	
	count_char = password.count(char)

	if count_char >= lower_bound and count_char <= upper_bound:
		valid_count += 1
	

print("valid count: " , valid_count)

			
