s = "abcdef"

# 打印字符串长度（len）
print(len(s))

# 正向切片操作 "abc" 字符串变量[start，end（不包含end）]，左开右闭原则
print(s[:3])

# 反向切片操作 "def"
print(s[-3:])

# 掐头去尾 "bcde"
print(s[1:-1])

# s[::4],代表从头到尾,step为4进行取值，step正数为正向取值，负数为反向取值
print(s[::-4])

# find、rfind用法，index、rindex也可用于查找
# find与index区别，find未找到返回-1，index未找到报错
addr = "http://www.baidu.com_adhjsdjkldland.git"
i = addr.find("_")
addr_name = addr[i + 1:]
print(addr_name)

j = addr.rfind(".")
addr_name = addr[j + 1:]
print(addr_name)

# count 统计字符出现的次数
k = addr.count(".")
print(k)

'''
字符串判断函数:
startswith，endswith，
isalpha 是否全部是字母，返回True或False
isdigit 是否全部是数字，返回True或False
isalnum 是否是字母+数字组合，返回True或False
isspace 是否是空白字符串，返回True或False
'''
result = addr.startswith("htt")
print(result)
result = addr.endswith("htt")
print(result)