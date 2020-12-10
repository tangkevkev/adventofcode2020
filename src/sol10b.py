def recursion(last_index, cur_index, joltages, dp):	

	if cur_index >= len(joltages):
		return 0
	if cur_index == len(joltages)-1:
		if joltages[cur_index] - joltages[last_index] <= 3:
			return 1
	if joltages[cur_index] - joltages[last_index] > 3:
		return 0
	
	if(dp[cur_index] > 0):
		return dp[cur_index]
	total = 0
	for i in range(1,4):
		total += recursion(cur_index, cur_index+i, joltages, dp)
	dp[cur_index] = total
	return total

fileObj =  open('../input/input10.txt', 'r')
numbers = fileObj.read().splitlines()

joltages = [0]
for num in numbers:
	joltages.append(int(num))

joltages = sorted(joltages)
#Add the final adapter
joltages.append(joltages[-1]+3)
diffs = [joltages[i+1] - joltages[i] for i in range(len(joltages)-1)]
dp = [-1 for i in range(len(joltages))]
print(recursion(0,0,joltages,dp))

