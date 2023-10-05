# 可变类型：
# 不可变类型：对象在内存中所指向的值是不可变的
# 不可变：int str float tuple(元组)

# 可变类型：对象在内存中所指向的值是可变的
# 可变：list dict set
set = {1, 2, 3, 4, 5}
print(set,id(set))

set.pop()
print(set,id(set))
