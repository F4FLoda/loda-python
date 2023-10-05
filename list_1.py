# 空列表
list1 = []

# 获取列表信息,用下标索引
list2 = [1, 2, 3, 4, 5]
print(list2[2])
print(list2[-1])
# 切片
print(list2[:2])
print(list2[-3:])
# 添加元素 append
list2.append(6)
print(list2)
# 删除并保存打印删除的数据 pop remove clear
list2_pop = list2.pop()
print(list2)
print(list2_pop)
# pop(index) 下标
list2.pop(2)
print(list2)
# remove(element) 元素值
list2.remove(5)
print(list2)
list2.clear()
print(list2)