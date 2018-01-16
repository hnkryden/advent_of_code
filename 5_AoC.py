
file = open("input_5.txt",'r')

lines = file.readlines()

instr = [int(x) for x in lines]


print('Day 5')

i = 0
steps = 0
while i< instr.__len__():
    new_i = instr[i]
    instr[i] += 1
    i = i + new_i
    steps += 1
    if(i<0):
        break

print("A :" + str(steps))



instrB = [int(x) for x in lines]

i = 0
steps_B = 0
while i< instrB.__len__():
    new_i = instrB[i]
    instrB[i] += 1 if new_i < 3 else -1
    i = i + new_i
    steps_B += 1
    if(i<0):
        break
print("B : " +str(steps_B))
