
file = open('data/2.txt','r')
data = file.readlines()

hor=0
dep=0
aim=0
for row in data:
    elem = row.split()
    val = int(elem[1])
    if elem[0]=='forward':
        hor += val
        dep += val * aim
    elif elem[0]=='down':
        aim += val
    elif elem[0]=='up':
        aim -= val
print(hor*dep)

    
