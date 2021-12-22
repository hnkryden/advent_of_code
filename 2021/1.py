
file = open('data/1.txt','r')
data = file.readlines()
data = [int(i) for i in data]
res = 0
for i in range(1,len(data)):
    if data[i]>data[i-1]:
        res+=1
print(res)
resB = 0
for i in range(3,len(data)):
    resB += sum(data[(i-3):i]) < sum(data[(i-2):(i+1)]) 
print(resB)