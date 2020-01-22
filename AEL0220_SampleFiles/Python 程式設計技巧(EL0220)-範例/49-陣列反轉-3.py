# 49-陣列反轉-3 (飆程式網 #1011) -3
# n=int(input())
# ipline=input()
n=5
ipline='2 3 12 4 5'
ipline=' '+ipline+' '

numlist=[]
strlen=len(ipline)
c=0 ;k=0 ; l=0;  r=0

for i in range(strlen):
    if ipline[i]==' ':
        l=k; r=i
        k=r
        c=c+1
        if c>1 :
            numlist.append(int(ipline[l+1:r]))
numlist.reverse()
c=len(numlist)
for i in range(c):
    if i<c-1 :
        print(str(numlist[i])+' ', end='')
    else:
        print(str(numlist[i]), end='')
