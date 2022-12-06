input = open('input.txt','r')

maxcalorie = 0
currentcalorie = 0
goblinCalorieList = []
topthreegoblins = 0
for x in input:
    if (x == "\n"):
        if currentcalorie > maxcalorie:
            maxcalorie =  currentcalorie
        goblinCalorieList.append(currentcalorie)
        currentcalorie = 0
    else:
        currentcalorie += int(x.replace('\n','0'))/10
        #print(currentcalorie)


goblinCalorieList.sort(reverse=True)
topthreegoblins = goblinCalorieList[0]+goblinCalorieList[1]+goblinCalorieList[2]
print(f"Part A: {maxcalorie}" )
print(f"Part B: {topthreegoblins}")



