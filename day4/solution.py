input=open("input.txt",'r')
count=0
# split the input into a list of characters and remove the newline character
for line in input:
    line=line.split("\n")[0]
    # split the string into a list of strings
    n1 = int(line.split("-")[0])
    n2 = line.split("-")[1]
    n3 = n2.split(",")[1]
    n2 = int(n2.split(",")[0])
    n4 = int(line.split("-")[2])
    n3 = int(n3)
    #print(n1,n2,n3,n4)
    if n1 >= n3 and n2 <= n4:
        count+=1
        print(n1,n2,n3,n4)
    elif n1 <= n3 and n2 >= n4:
        count+=1
        #print(n1,n2,n3,n4)


print(count)

