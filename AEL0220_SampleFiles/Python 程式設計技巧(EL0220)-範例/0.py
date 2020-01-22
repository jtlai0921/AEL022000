# 遞迴算二進位
 
def dtb(n):
    if n > 1:
        dtb(n//2)
    print(n % 2,end = '')
   
# 輸入進位數
dec = 1
dtb(dec)

