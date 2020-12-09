fileObj =  open('../input/input9.txt', 'r')
lines = fileObj.read().splitlines()

preamble_length = 25
cipher = []

for line in lines:
    cipher.append(int(line))

for i in range(preamble_length, len(lines)):
    last_interval = cipher[i-preamble_length:i]
    cur_number = cipher[i]

    exist_sum = False

    for s in range(0,preamble_length):
        for t in range(0,preamble_length):
            if s != t:
                if last_interval[s] + last_interval[t] == cur_number:
                    exist_sum = True
                    break
        if exist_sum:
            break

    if not exist_sum:
        print(cur_number)
        break        
