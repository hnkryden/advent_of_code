# AoC 9
file = open("input_9.txt")
str = file.readline()

#str = 'abc!!!de<f>asdsad'
# Remove !
while True:
    index = str.find('!')
    if(index ==-1 ):
        break
    str = str[0:index] + str[(index+2):]

print(str+"\n")

# Remove garbage

score_b = 0
while True:
    indexStart = str.find('<')
    indexStop  = str[indexStart:].find('>')
    if (indexStart == -1) or (indexStop == -1):
        break
    str = str[0:indexStart] + str[indexStart+indexStop+1:]
    score_b += (indexStop -1)

depth = 0
score = 0
for i in range(str.__len__()):
    if(str[i]=='{'):
        depth += 1
    elif (str[i]=='}'):
        score += depth
        depth -= 1
print(" A = ",score)
print(" B = ",score_b)




