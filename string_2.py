s = "abcdefgh aa bb cc"
# replace 替换
result = s.replace("a", "**")
print(result)

# split rsplit 切割字符串,split("分隔符")，返回的结果是一个列表list
result = s.split(" ")
print(result)
result = s.rsplit(" ")
print(result)

# 字符串函数 首字母大写title，全部大写upper，全部小写lower
print(s.title())
print(s.upper())
print(s.lower())

# strip处理空格字符, lstrip/rstrip
b = " abc  "
print(b.strip())

name = "李雷"
age = 18
print("少年{}，今年{}岁".format(name, age))
# 使用数字填充，从0开始计数
print("少年{0}，今年{1}岁，我也{1}岁".format(name, age))
# 变量名的形式，format参数必须是关键字参数
print("少年{name}，今年{age}岁，我也{age}岁".format(name="李雷", age=18))
