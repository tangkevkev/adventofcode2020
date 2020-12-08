fileObj =  open('../input/input8.txt', 'r')
lines = fileObj.read().splitlines()

instructions = []
original_instructions = []
for line in lines:
    (inst, arg) = line.split(' ')
    instructions.append((inst, arg))
    original_instructions.append((inst, arg))



for i in range(0, len(instructions)):
    terminated = False
    cur_instruction = 0
    accumulator = 0
    visited_instruction = set()

    #Copy by value
    instructions = original_instructions[:]
    if(instructions[i][0] == 'jmp'):
        instructions[i]= ('nop', instructions[i][1])
    elif(instructions[i][0] == 'nop'):
        instructions[i] = ('jmp', instructions[i][1])
    else:
        continue

    while True:

        #Instruction visited twice => loop 
        if cur_instruction in visited_instruction:
            break
        
        if cur_instruction == len(instructions):
            terminated = True
            break

        (inst, arg) = instructions[cur_instruction]
        visited_instruction.add(cur_instruction)
        if inst == 'nop':
            cur_instruction += 1
            continue
        elif inst == 'acc':
            accumulator += int(arg)
            cur_instruction += 1
        elif inst == 'jmp':
            cur_instruction += int(arg)
    
    if terminated:
        terminated = False
        print(accumulator)
