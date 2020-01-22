#1050305-10

def g(a):
    if (a>1):
        return g(a-2)+3
    return a

print("g(13)=",g(13))


