# AoC 7

file = open("input_7.txt",'r')


lines = file.readlines()



def part_A(lines):
    d_weight = dict()
    d_is_bottom = dict()
    for line in lines:
        elems = line.split()
        bottom = elems[0]
        d_is_bottom[bottom] = 1


    for line in lines:
        elems = line.split()
        bottom = elems[0]
        weight = elems[1].strip('()')
        d_weight[bottom] = weight
        if(elems.__len__()>2):
            for tmp in elems[3:]:
                tmp = tmp.strip(',')
                d_is_bottom[tmp] = 0
        else:
            d_is_bottom[bottom] = 0

    for key,value in d_is_bottom.items():
        print(key,value) # one will have a zero


def check_sum(cur, d_rel,_d_weight):
    if(len(d_rel[cur])==0):
        return _d_weight[cur]
    else:
        sum_weight = _d_weight[cur]
        for next in d_rel[cur]:
            sum_weight += check_sum(next,d_rel,_d_weight)
        return sum_weight


def part_B(lines):
    d_weight = dict()
    d_rel = dict()

    for line in lines:
        elems = line.split()
        bottom = elems[0]
        weight = int(elems[1].strip('()'))
        d_weight[bottom] = weight
        d_rel[bottom] = []
        if (elems.__len__() > 2):
            for tmp in elems[3:]:
                d_rel[bottom].append(tmp.strip(','))
    # Find error
    for key,value in d_rel.items():
        if(len(d_rel[key])>0):
            res = []
            for k in d_rel[key]:
                res.append(check_sum(k,d_rel,d_weight))
            if(set(res).__len__()>1):
                print(key,res)
    return d_weight,d_rel



d_weight, d_rel = part_B(lines)
print("end")
# Some manual job, rugzyaj is wrong
new_weight = d_weight[d_rel['rugzyaj'][0]] - (1579-1571)
print(new_weight)