input = open('input.txt','r')

# ASCII value of a - 97 and z - 122 => difference of 96 to obtain prio
# ASCII value of A - 65 and Z - 90  => difference of 38 to obtain prio
t=0
t2 =0
line3 = []
lol = []
f=0
for line in input:
    line = line.strip()
    line = [*line]
    x = len(line) 
    a = line[:x//2]
    b = line[x//2:]
    k, = set(a) & set(b)
    if k >= "a":
        t += ord(k) - ord("a") + 1
    else:
        t += ord(k) - ord("A") + 27
    #PartB
    line3 = line3 + line
    lol.append(x)
    f = f +1
    if f == 3:
        p = line3[:lol[0]]
        q = line3[lol[0]:lol[0]+lol[1]]
        r = line3[lol[0]+lol[1]:sum(lol)]
        z,= set(p) & set(q) & set (r)
        if z >= "a":
            t2 += ord(z) - ord("a") + 1
        else:
            t2 += ord(z) - ord("A") + 27
        f = 0 
        line3.clear()
        lol.clear()

print(" Part A :",t,'\n','Part B :',t2)
