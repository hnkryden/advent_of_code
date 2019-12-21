# AoC 12

file = open("input_12.txt",'r')
#file = open("tmp.txt",'r')
lines = file.readlines()

d = dict()
d_a = dict() # Visited cells
for line in lines:
    elem = line.split("<->")
    base = elem[0].strip()
    if not (base in d):
        d[base]=[]
        d_a[base] = False
    for rel in elem[1].strip().split(', '):
        if not (rel in d):
            d[rel] = []
            d_a[rel] = False
        d[base].append(rel)
        d[rel].append(base)

lst = ['0']
relations = 0
while len(lst)>0:
    cur = lst.pop()
    if not d_a[cur]:
        lst.extend(d[cur])
        relations += 1
        d_a[cur] = True

print("A = ",relations)

# b, groups not in '0'
nrofGroups = 1

while not all(d_a.values()):
    lst = [next((key for key, val in d_a.items() if not val), None)]
    while len(lst) > 0:
        cur = lst.pop()
        if not d_a[cur]:
            lst.extend(d[cur])
            relations += 1
            d_a[cur] = True
    nrofGroups += 1
print(nrofGroups)


