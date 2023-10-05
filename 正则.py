# 正则表达式：regex或RE，正则验证的是字符串，不能是其他类型
import re

msg = "du2at6ihtone"
result = re.match("tone", msg)  # match从头开始匹配，如果匹配不成功立刻返回None
print(result)

result = re.search("tone", msg)  # search匹配整个字符串
print(result)
print(result.span())
print(result.group())  # group提取匹配的内容

result = re.search("[a-z][0-9][a-z]", msg)  # search找到一个就不继续往下找了
print(result)
result = re.findall("[a-z][0-9][a-z]", msg)  # findall找到全部符合条件的
print(result)

# 正则验证次数 * + ？{m,n}          *表达≥0 +表示≥1 ？表示0或1  {m,n}表示m≤次数≤n
msg1 = "dasf2fg43se1hg32kg55jd832d"
result = re.findall("[a-z][0-9]+[a-z]", msg1)  # +在谁的后面就表示谁出现的次数大于等于1次
print(result)

# [0-9] = \d
qq = "595811947"
result = re.match("^[1-9]\d{4,10}$", qq)
print(result)

# 练习：用户名6位以上，数字和字母组成，首位不能是数字
# [0-9a-zA-Z_] = \w
username = "admin001"
result = re.match("[a-zA-Z]\w{5,}$", username)  # ^表示从头开始匹配，$表示匹配到结尾
print(result)


a = "aa.py ee.exe bb.py cc.png dd.doc vv.py"
result = re.findall(r"py\b",a)
print(result)

'''
总结：
. 任意字符
^ 开头
$ 结尾
[] 范围
    [0-9a-zA-Z_] = \w
    [0-9] = \d
\s 空格   \S  非空格
\b 边界   \B  非边界
\d 数字   \D  非数字
\w 字母和_     
* ≥0
+ ≥1
？0或1
{m,n} m≤次数≤n
'''

# 手机号正则验证
# re.match("1[35789]\d{9}$",phone)