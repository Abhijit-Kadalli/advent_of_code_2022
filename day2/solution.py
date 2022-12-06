input = open('input.txt','r')
#part A
points =0
# A and X rock    1 pt      win  = 6 pt
# B and Y paper   2 pt      draw = 3 pt
# C and Z scissor 3 pt      loss = 0 pt
shape = {
    ('A','X'):4,('B','X'):1,('C','X'):7,
    ('A','Y'):8,('B','Y'):5,('C','Y'):2,
    ('A','Z'):3,('B','Z'):9,('C','Z'):6
}

#part B
# X = lose the round
# Y = draw
# Z = win
pointsB = 0
weights = {
    ('A','Y'):4,('B','X'):1,('C','Z'):7,
    ('A','Z'):8,('B','Y'):5,('C','X'):2,
    ('A','X'):3,('B','Z'):9,('C','Y'):6
}
for x in input:
    x = x.split()
    points +=shape[(x[0],x[1])]
    pointsB+=weights[(x[0],x[1])]


print(f"Part a: {points}")
print(f"Part b: {pointsB}")