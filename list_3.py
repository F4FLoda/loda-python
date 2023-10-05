# sort和reverse
import random
num = []
for i in range(8):
    ran = random.randint(1, 100)
    num.append(ran)
print(num)
# sort默认升序
num.sort()
print(num)
# reverse 两种用法:1.翻转列表 2.作参数用:默认为False
num.sort(reverse=True)
print(num)
num.reverse()
print(num)