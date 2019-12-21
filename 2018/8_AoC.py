

file = open("input_8.txt",'r')

lines = file.readlines()
d = dict()
max_b = 0
for line in lines:
    elem = line.split()
    reg_change = elem[0]
    if not reg_change in d:
        d[reg_change] = 0
    if not elem[4] in d:
        d[elem[4]] = 0

    operator = '-1*' if (elem[1]=='dec') else ''

    d[reg_change] += eval(operator+' '.join(elem[2:4])+' '+'d["'+elem[4]+'"] ' + ' '.join(elem[5:]) + ' else 0')
    if(d[reg_change]>max_b):
        max_b = d[reg_change]


maxVal = sorted(d.items(), key=lambda x: x[1])[-1]
print("A",maxVal)
print("B",max_b)
