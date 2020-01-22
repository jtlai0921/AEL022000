#1050305-3
def f1(a, value,c):
    i=0 ;  r_value = -1
    while ( i < 100 ):
        c += 1
        if (a[i] == value):
            r_value = i
            break
        i += 1
    return  c

def  f2(a,value,c):
    low=0 ; high=99
    while (low <= high):
        c += 1
        mid = (low + high)//2
        if  (a[mid] == value):
            r_value = mid
            break
        elif  (a[mid] < value):
            low = mid + 1
        else:
            high = mid -1
    return  c

#main
a=[] ; value=100 ;n1=0 ; n2=0
for k in range(100):
    a.append(3*k+1)

n1=f1(a,value,n1)
n2=f2(a,value,n2)
print("n1=%d, n2=%d" %(n1,n2))

