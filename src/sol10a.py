fileObj =  open('../input/input10.txt', 'r')
numbers = fileObj.read().splitlines()

joltages = [0] + sorted([int(num) for num in numbers])
#Add the final adapter
joltages.append(joltages[-1]+3)
diffs = [joltages[i+1] - joltages[i] for i in range(len(joltages)-1)]

result = diffs.count(1)*diffs.count(3)
print(result)

