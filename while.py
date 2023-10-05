import random as rd

ran = rd.randint(1, 50)
guess = int(input("输入；"))
if guess == ran:
    print("猜对了")
else:
    print("猜错了")

