# AoC 24
file = open("input_24.txt",'r')
#file = open("tmp.txt",'r')

#lines = [line.rstrip() for line in file.readlines()]

ports = []

for line in file.readlines():
    elem = [int(x) for x in line.split('/')]
    ports.append(elem)

def find_best(cur,avail,lst):
    best = []
    for i in range(len(lst)):
        if (cur[avail] in lst[i]):
            next_avail = 0 if cur[avail]==lst[i][1] else 1
            maxNext = sum(cur) + find_best(lst[i],next_avail, [x for j,x in enumerate(lst) if j!=i] )
            best.append(maxNext)
    if(len(best)==0):
        return sum(cur)
    return max(best)

idx_0=11
cur = ports[idx_0]
ports = [x for j,x in enumerate(ports) if j!=idx_0]

best_a = find_best(cur,1,ports)
print(best_a)


def find_best_b(cur,avail,lst,depth):
    best = []
    for i in range(len(lst)):
        if (cur[avail] in lst[i]):
            next_avail = 0 if cur[avail]==lst[i][1] else 1

            [maxNext, depth_next] = find_best_b(lst[i],next_avail, [x for j,x in enumerate(lst) if j!=i] ,depth+1)
            best.append([maxNext+sum(cur), depth_next +1])
    if(len(best)==0):
        return [sum(cur),1]
    max_depth = max([x[1] for x in best])
    index_max = [i for i in range(len(best)) if best[i][1] == max_depth]
    return [max([best[x][0] for x in index_max]),max_depth]

best_b = find_best_b(cur,1,ports,0)
print("B = ", best_b[0])