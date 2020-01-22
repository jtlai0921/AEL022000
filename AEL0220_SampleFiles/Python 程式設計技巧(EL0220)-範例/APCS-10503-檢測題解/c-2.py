#1050305-2

def f(a,n):
    index=0
    for i in range(1,n):
        if (a[i] >= a[index]): index=i
    return index

#main
a=[1,3,9,2,5,8,4,9,6,7]
print("回傳值為",f(a,10))


