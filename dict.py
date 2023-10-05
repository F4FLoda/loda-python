# 字典dictionary
dict1 = {}  # 空字典：使用最多
dict2 = dict()  # 空字典：（了解）
dict3 = {"ID": "1105",  "name": "li yang",  "age": 18}

# 增删查改
# 增加/修改元素：dict[key] = "value";如果有相应的key，则修改相应的value值
dict3["sex"] = "男"
# print(dict3)

# 查询元素,根据key找到元素：dict[key] = value
print(dict3["sex"])

# 遍历字典
# items(),values(),keys()
# items() -> 将字典的键值对转成list保存
for key, value in dict3.items():
    # print(key, value)
    pass

# values() -> 取出字典中所有的值，保存到列表中
for i in dict3.values():
    # print(i)
    pass

# keys() -> 取出字典中所有的键，保存到列表中
for j in dict3.keys():
    #print(j)
    pass

# 字典内置函数：get(key),如果取不到值，返回None；get(key，default)，如果取不到值，返回default值
print(dict3.get("ID"))
print(dict3.get("TX"))
print(dict3.get("TX", 99))

# 删除元素
# del dict[] （少用）
# dict.pop(key) 最多使用
# dict.popitem() 理论上随机删除，但一般从末尾删除
# dict.clear() 清空字典
dict3.pop("ID")
print(dict3)
dict3.popitem()
print(dict3)
dict3.popitem()
print(dict3)
dict3.clear()
print(dict3)

# 了解update() 字典合并的函数
# 了解fromkeys(seq)  将seq转换成字典的函数