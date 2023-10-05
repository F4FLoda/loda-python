# tuple元组使用()，list列表使用[]

# str ()里面只有一个元素为str
t1 = ('a')
print(type(t1))
# tuple ()只有一个元素时必须添加‘ ，’
t1 = ('a',)
print(type(t1))

t1 = (1, 2, 3, 4, 5, 6)
print(t1[2:])
# 逆序输出
print(t1[::-1])
