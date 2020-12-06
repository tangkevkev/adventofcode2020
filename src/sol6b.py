

fileObj =  open('../input/input6.txt', 'r')
lines = fileObj.readlines()
answer_count = 0

answer_per_group = set()
first_person = True

for i in range (0, len(lines)):
	line = lines[i]
	if line == '\n':
		first_person = True
		answer_count += len(answer_per_group)
		answer_per_group = set()
	else:
		joint_answer  = set()
		for answer in line:
			if answer != '\n':
				if first_person:
					answer_per_group.add(answer)
				else:
					if answer in answer_per_group:
						joint_answer.add(answer)
		if not first_person:
			answer_per_group = joint_answer
		
		first_person = False
			
		if i == len(lines)-1:
			answer_count += len(answer_per_group)




print(answer_count)

	
	


			
