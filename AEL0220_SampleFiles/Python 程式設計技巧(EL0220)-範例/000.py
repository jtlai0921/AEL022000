#飆程式網1010 : 找出最小值
# n=int(input())
# ipline=input()
n=5
ipline='6 3 4 17 9'
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
            numlist.append \
            (int(ipline[l+1:r]))
print(min(numlist))
