import math

def computeFuel(mass):
    return math.floor(mass/3)-2



fobj = open("input1.txt","r")
totalFuel = 0
for line in fobj:
    currentFuel = computeFuel(int(line))        
    while(currentFuel>0):
        print(currentFuel, totalFuel)
        totalFuel = totalFuel + currentFuel
        currentFuel = computeFuel(currentFuel)    
fobj.close()
print(totalFuel)

   