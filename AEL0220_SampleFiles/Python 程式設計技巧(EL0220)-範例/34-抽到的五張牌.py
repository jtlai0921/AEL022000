# 發牌
import itertools, random

# 花色
deck = list(itertools.product(range(1,14),['黑桃','紅心','方塊','梅花']))

# 洗牌
random.shuffle(deck)

# 抽五張牌
print("所抽到的五張牌是:")
for i in range(5):
   print(deck[i][1],":",deck[i][0])
