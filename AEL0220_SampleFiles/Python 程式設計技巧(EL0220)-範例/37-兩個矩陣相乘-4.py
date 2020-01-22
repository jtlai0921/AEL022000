# 兩個矩陣相乘 (值得思考 有點難度)

'''
https://goo.gl/pP2KbL

可到這裡驗證 
https://goo.gl/EyZ3Bf

本題矩陣相乘 結果圖形
https://i.imgur.com/Xae6kWn.jpg

 59  63  49
 74  79  73
 94  90 107

X =
(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)

Y =
(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)

X*Y=
x(0,0)*y(0,0)+x(0,1)*y(1,0)+x(0,2)*y(2,0)  x(0,0)*y(0,1)+x(0,1)*y(1,1)+x(0,2)*y(2,1)  x(0,0)*y(0,2)+x(0,1)*y(1,2)+x(0,2)*y(2,2)
x(1,0)*y(0,0)+x(1,1)*y(1,1)+x(1,2)*y(2,0)  x(1,0)*y(0,1)+x(1,1)*y(1,1)+x(1,2)*y(2,1)  x(1,0)*y(0,2)+x(1,1)*y(1,2)+x(1,2)*y(2,2)
x(2,0)*y(0,0)+x(2,1)*y(1,0)+x(2,2)*y(2,0)  x(2,0)*y(0,1)+x(2,1)*y(1,1)+x(2,2)*y(2,1)  x(2,0)*y(0,2)+x(2,1)*y(1,2)+x(2,2)*y(2,2)                                      ...   ...

'''

# 設定 X 陣列
X = [[1,7,3],
    [4 ,5,6],
    [2 ,8,9]]

# 設定 Y 陣列
Y = [[5,8,1],
    [6,7,3],
    [4,2,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

print('印出 X')
for i in range(3):
    for j in range (3):
        print(X[i][j], end=' ')
    print()
print()


print('印出 Y')
for i in range(3):
    for j in range (3):
        print(Y[i][j], end=' ')
    print()
print()    

m1=0;m2=0;m3=0
for i in range(3):
    for j in range(3):
        m1=m1+X[i][j]*Y[j][0] # 印出數值
        m2=m2+X[i][j]*Y[j][1]
        m3=m3+X[i][j]*Y[j][2]
    result[i][0]=m1           # 填入陣列值
    result[i][1]=m2
    result[i][2]=m3 
    print('%3d %3d %3d' % (m1,m2,m3)) # 印出結果
    m1=0;m2=0;m3=0
    print()

for r in result:             # 印出陣列值
   print(r)


    
        
