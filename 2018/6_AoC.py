seq = [4,1,15,12,0,9,9,5,5,8,7,3,14,5,12,3]



def new_seq(seqTmp):
    val = max(seqTmp)
    idx = seqTmp.index(val)
    seqTmp[idx] = 0
    idx+=1
    while val>0:
        seqTmp[idx % len(seqTmp)] += 1
        idx += 1
        val -= 1
    return seqTmp

def convertSeq(seqTmp):
    return ','.join(str(x) for x in seqTmp)


seqLst = []
seqLst.append(convertSeq(seq))
steps = 0
while seqLst.__len__() == set(seqLst).__len__():
    seq_new = new_seq(seq)
    seq = seq_new
    seqLst.append(convertSeq(seq_new))
    steps += 1

print("A steps: " + str(steps))
b_steps = 0
b_seq = seqLst[-1]
seq_new = ''
while b_seq != convertSeq(seq_new):
    seq_new = new_seq(seq)
    seq = seq_new
    seqLst.append(convertSeq(seq_new))
    b_steps += 1

print("B steps: " + str(b_steps))
