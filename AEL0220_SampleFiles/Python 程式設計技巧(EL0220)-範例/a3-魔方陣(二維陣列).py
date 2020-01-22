# 奇數魔方陣(二維陣列)

a =int(input("請輸入方陣數值單數(3~15)="))
ary=[ [0] * (a+1) for i in range(a+1) ]
r = 1
c = int((a + 1) / 2)
numb = 1

ary[c][r]=numb
for i in range(1 , (a * a) ):
    r = r - 1; c = c + 1
    if (r<1) :
        r=a
    if (c>a) :
        c=1
    numb = numb + 1
    if (ary[c][r] != 0 ):
        c = c - 1; r = r + 2
        if (c<1) :
            c=a
        if ( r>a):
            r=r-a
        ary[c][r] = numb
        # print (c, r, numb)
    else:
        ary[c][r] = numb
        # print (c, r, numb)

for i in range(1,a+1):
    for j in range(1,a+1):
        if ( ary[j][i] < 10 ):
            print( " ",end='')
        print(ary[j][i],end=' ')
    print()
