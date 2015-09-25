l  = [0,1,2,3,4,5,6]

def roatationR(pos):
    print l[pos:]+l[:pos]
roatationR(2)

currentNum = 4
pos = 2
length = len(l)
tmpl = 3*l
currentList = []
for i in [-2,-1,0,1,2]:
    currentList.append(tmpl[currentNum+i+length])

print currentList
pos = currentList.index(pos)-2
if pos>0:
   pass
elif pos < 0:
   pass     
