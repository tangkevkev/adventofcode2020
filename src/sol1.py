

fileObj =  open('../input/input1.txt', 'r')
numbers = fileObj.read().splitlines()

for i in numbers:
	for j in numbers:
		for k in numbers:
			k_num = int(k)
			i_num = int(i)
			j_num = int(j)
			if(i_num+j_num+k_num == 2020):
				print(i_num*j_num*k_num)
				exit(0)
			
