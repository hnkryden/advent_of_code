
# AoC 4

file = open("input_4.txt")


valid_line = 0
for line in file.readlines():
    elem = line.split()
    tmp = set(elem)
    if(elem.__len__()==tmp.__len__()):
        valid_line += 1

print("A Number of valid lines "+str(valid_line))

# Part B
file = open("input_4.txt")

valid_line_B = 0
for line in file.readlines():
    elem = line.split()
    sorted_elem = [''.join(sorted(x)) for x in elem]
    tmp = set(sorted_elem)
    if(elem.__len__()==tmp.__len__()):
        valid_line_B += 1

print("B Number of valid lines "+str(valid_line_B))
