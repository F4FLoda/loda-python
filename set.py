# 集合 set    作用：去重
s1 = set()  # 空集合 创建空集合只能用set()
# 添加元素 add update
s1.add("hello")
s1.add(" ")
s1.add("world")
print(s1)
# 删除元素 remove(报异常) pop(随机删除) clear(清空) discard(不会报异常)
s1.remove(" ")
print(s1)
# pop()随机删除，一般删除首元素
s1.pop()
print(s1)
s1.clear()  # 清空集合

# == 判断两个集合中的元素是否相等
set2 = {1, 2, 3, 4, 5}
set3 = {1, 2, 3, 4, 5, 6}

# -:差集  difference()
set4 = set3 - set2
print(set4)
set5 = set3.difference(set2)
print(set5)

# & 交集  intersection()
set4 = set3 & set2
print(set4)
set5 = set3.intersection(set2)
print(set5)

# | 并集  union()
set4 = set3 | set2
print(set4)
set5 = set3.union(set2)
print(set5)

# ^ 对称差集：两个集合不同的部分 symmetric_difference()
l1 = [1, 2, 4, 6, 7, 8]
l2 = [3, 4, 6, 7, 8, 10]
s1 = set(l1)
s2 = set(l2)
s3 = s1 ^ s2
print(s3)
s4 = s1.symmetric_difference(s2)
print(s4)
