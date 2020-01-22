import sys

while True:
    print('input 單筆數字 n: ',end='')
    n=int(sys.stdin.readline().strip('\n'))
    print('input 多筆數字 listA: ',end='')
    listA=sys.stdin.readline().strip()
    if listA=='':
        break
    listA=list(map(int,listA.split()))
    print(n)
    print(listA,'\n')

    
      

      
