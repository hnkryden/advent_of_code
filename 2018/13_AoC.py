# AoC 13
import math
import numpy as np
file = open("input_13.txt",'r')
#file = open("tmp.txt",'r')

lines = file.readlines()
nrofLayers = 99
#nrofLayers = 7

layer = np.zeros(nrofLayers)
scanners_depth = [0 for x in range(nrofLayers)]
for line in lines:
    elem = [int(x.strip()) for x in line.split(': ')]
    layer[elem[0]] = elem[1]

caught = 0
index_0 = np.where(layer > 0)[0]

for pos in range(nrofLayers):
    if(scanners_depth[pos]==0):
        caught += pos*layer[pos]
    scan_movement = np.zeros(nrofLayers)

    scan_movement[index_0] = [1 if (math.floor((pos/(layer[x]-1))) % 2) == 0 else -1 for x in index_0]
    scanners_depth += scan_movement
print("A = ",int(caught))


delay = 0
scanners_depth_delay = [0 for x in range(nrofLayers)]

while True:
    caught = False
    if(delay>0):
        scan_movement = np.zeros(nrofLayers)
        scan_movement[index_0] = [1 if (math.floor(((delay-1) / (layer[x] - 1))) % 2) == 0 else -1 for x in index_0]
        scanners_depth_delay += scan_movement
    scanners_depth = list(scanners_depth_delay)

    for pos in range(nrofLayers):
        if (scanners_depth[pos] == 0) and (layer[pos]>0):
            caught = True
            break
        scan_movement = np.zeros(nrofLayers)
        scan_movement[index_0] = [1 if (math.floor(((delay + pos) / (layer[x] - 1))) % 2) == 0 else -1 for x in index_0]
        scanners_depth += scan_movement
    if(not caught):
        break
    delay+=1
    if(delay%10000 == 0 ):
        print(delay)

print("B ",delay)
