file = open("input.txt",'r')
#A & B
checksum = 0
divideSum = 0
for line in file.readlines():
    lineInt = [int(str) for str in line.split()]
    #A
    checksum += max(lineInt) - min(lineInt)
    lineInt.sort()
    for i in range(0,len(lineInt)-1):
        for j in range(i+1,len(lineInt)):
            if (lineInt[j] % lineInt[i]) ==0:
                divideSum += lineInt[j] / lineInt[i]

print(checksum,divideSum)