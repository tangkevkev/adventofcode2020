fileObj =  open('../input/input9.txt', 'r')
lines = fileObj.read().splitlines()

preamble_length = 25
cipher = []

target_sum = 1309761972


for line in lines:
    cipher.append(int(line))

for i in range(preamble_length, len(lines)):
    last_interval = cipher[i-preamble_length:i]

    exist_sum = False

    for s in range(0,preamble_length):
        cur_sum = last_interval[s]
        for t in range(s+1, preamble_length):
            cur_sum += last_interval[t]
            if cur_sum == target_sum:
                result = min(last_interval[s:t+1]) + max(last_interval[s:t+1])
                print(result)
                exist_sum = True
                break
        if exist_sum:
            break

    if exist_sum:
        break        
