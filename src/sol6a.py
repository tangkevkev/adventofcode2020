

fileObj =  open('../input/input6.txt', 'r')
lines = fileObj.readlines()
answer_count = 0

answer_per_group = set()


for i in range (0, len(lines)):
	line = lines[i]
	if line == '\n':
		answer_count += len(answer_per_group)
		answer_per_group = set()
	else:
		for answer in line:
			if answer != '\n':
				answer_per_group.add(answer)
		if i == len(lines)-1:
			answer_count += len(answer_per_group)




print(answer_count)

	
	


			
