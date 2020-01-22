# 用泰勒級數計算圓周率
# π=2x(1+1/3+2/5+3/7+4/9+5/11+.........)

import math

def pi(a):
    x=2;z=2;a=1;b=3;e=1e-15
    while(z>e):
        z = z*a/b
        x=x+z
        a=a+1
        b=b+2
    return x 

print(pi(0))
print(math.pi)


