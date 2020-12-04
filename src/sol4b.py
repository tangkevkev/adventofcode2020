

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
		value = entry.split(':')[1].strip()


		if key == 'byr':
			if not(len(value) == 4):
				is_valid = False

			try:
				year = int(value)
				if year < 1920 or year > 2002:
					is_valid = False
	
			except ValueError:
				is_valid = False
		
		elif key == 'iyr':
			if not(len(value) == 4):
				is_valid = False
			try:
				year = int(value)
				if year < 2010 or year > 2020:
					is_valid = False

			except ValueError:
				is_valid = False	

		
		elif key == 'eyr':
			if not(len(value) == 4):
				is_valid = False

			try:
				year = int(value)
				if year < 2020 or year > 2030:
					is_valid = False

			except ValueError:
				is_valid = False
	
		elif key == 'hgt':
			unit = value[-2:]
			try:
				height = int(value[:-2])
			except ValueError:
				is_valid = False
		
			if unit =="cm":
				if height < 150 or height > 193:
					is_valid = False

			elif unit == 'in':
				if height < 59 or height > 76:
					is_valid = False

			else:
				is_valid = False

		elif key == 'hcl':
			if not(len(value) == 7) or not(value[0] == '#') :
				is_valid = False

			valid_char = ['0','1','2','3', '4','5','6','7','8','9','a','b','c','d','e','f']
			for char in value[1:]:
				if char not in valid_char:
					is_valid = False
					break
		elif key == 'ecl':
			valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
			if value not in valid_ecl:
				is_valid = False
		
		elif key == 'pid':
			if not(len(value) == 9):
				is_valid = False

			try:
				pid = int(value)
			except ValueError:
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
		continue
	
	


print("valid count: " , valid_count)

			
