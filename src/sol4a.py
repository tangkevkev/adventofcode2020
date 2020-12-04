

fileObj =  open('../input/input4.txt', 'r')
lines = fileObj.readlines()
valid_count = 0

key_set = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
cur_key_set = set()
is_valid = True


for i in range(0, len(lines)):
	line = lines[i]
	entries = line.split(' ')

	for entry in entries:
		if entry == '\n':
			continue
		key = entry.split(':')[0]
		if not (key in key_set):
			is_valid = False
		cur_key_set.add(key)
	
	if entries[0] == '\n' or i == len(lines)-1:
		if is_valid:
			if len(cur_key_set)+1 == len(key_set) and ("cid" in cur_key_set):
				is_valid = False	
			elif len(cur_key_set) < len(key_set)-1:
				is_valid = False	
		
		if is_valid:
			valid_count +=1
		
		is_valid = True
		cur_key_set = set()
		
	
	
	


print("valid count: " , valid_count)

			
