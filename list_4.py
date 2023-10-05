import random
num = []
num_1 = int(input("请输入数字："))
for i in range(8):
    ran = random.randint(1,100)
    num.append(ran)
num.append(num_1)
num.sort()
print(num)


