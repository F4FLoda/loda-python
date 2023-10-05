# n = 0x558
#
# print(int(n))
# print(bin(n))
# print(oct(n))
# x = 0b11110110
# print(hex(x))
# a = 0b0101
# b = 0b1001
# print(a & b)        # & 与
# print(a | b)        # | 或
# print(a ^ b)        # ^ 异或  相同为假，相异为真
# a = 9
# print(a << 2)
# print(a << 4)
# import random
#
# ran = random.randint(1, 10)
# print
# a = 10
# b = 20
# c = a if a > b else b           #三元操作符
# print(a, b, c)
# 打印1-50之间能被3整除的数
a = 1
# b = a % 3
while a <= 50:
    if a % 3 == 0:
        print(a)
    a += 1
