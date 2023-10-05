# 分组
import re

n = "100"
result = re.match(r"[1-9]?\d?$|100$",n)     # |或者
print(result)

# 邮箱验证
email = 'f4f_loda@163.com'
result = re.match(r"\w{5,11}@(163|126|qq)\.(com|cn)$",email)      # ()表示一个整体
print(result)

# 爬虫
phone = "022-88658049"
result = re.match(r"(\d{3}|\d{4})-(\d{8})$",phone)
print(result.group())
print(result.group(1))
print(result.group(2))

# 分组：起名的方式：(?P<名字>正则)(?P=名字)
msg = "<html><h1>python<h1><html>"
result = re.match(r"<(?P<name1>\w+)><(?P<name2>\w+)>(.+)<(?P=name2)><(?P=name1)>",msg)
print(result)
print(result.group(1))
print(result.group(3))

sub1 = "java"
result = re.sub(r"\w+","python",sub1)     # 替换
print(result)

# 贪婪和非贪婪
# 默认都是贪婪的，将贪婪变成非贪婪加'?'
