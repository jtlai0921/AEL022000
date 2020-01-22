# 發牌
import random

flower='♥♠♦♣'
nstr='A23456789TJQK'
c=[]
for i in range(0,52):
   c.append(i)
# print(c)

for i in range(0,51):
    s=random.randint(0,51)
    temp=c[i];c[i]=c[s];c[s]=temp
# print(c)

for i in range(0,52):
    f=c[i]//13; n=c[i]%13
    print(flower[f:f+1]+nstr[n],end=' ')
    if ( i%13==12):
        print()




