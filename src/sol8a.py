fileObj =  open('../input/input8.txt', 'r')
lines = fileObj.read().splitlines()

instructions = []
for line in lines:
    (inst, arg) = line.split(' ')
    instructions.append((inst, arg))

accumulator = 0
cur_instruction = 0
visited_instruction = set()

while True:
    (inst, arg) = instructions[cur_instruction]
    
    #Instruction visited twice => loop 
    if cur_instruction in visited_instruction:
        break
    
    visited_instruction.add(cur_instruction)
    if inst == 'nop':
        cur_instruction += 1
        continue
    elif inst == 'acc':
        accumulator += int(arg)
        cur_instruction += 1
    elif inst == 'jmp':
        cur_instruction += int(arg)

print(accumulator)
