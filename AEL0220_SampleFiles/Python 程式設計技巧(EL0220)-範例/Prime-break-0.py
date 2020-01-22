#找 1 ~ 100 所有的質數
for num in range(2,100):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print ( num, end=' ')


