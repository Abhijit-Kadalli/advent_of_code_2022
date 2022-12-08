input = open('input.txt','r')

# ASCII value of a - 97 and z - 122 => difference of 96 to obtain prio
# ASCII value of A - 65 and Z - 90  => difference of 38 to obtain prio
commonele = []
total = 0
for x in input:
    x = [*x]
    n = len(x)//2
    a = x[:n-1]
    b = x[n:]
    
    commonele = list(set(a) & set(b))
    commonele.append(0)
    commonele = commonele[0]
    
    if commonele != 0:
        temp = ord(commonele)
        if temp <90 and temp > 65:
            total = total + temp - 38
        elif temp >97 and temp < 122 :
            total = total + temp - 96 

print(total)