# random模块
import random
import hashlib
import requests
a = random.random()  # 产生0-1之间的随机小数
print(a)
b = random.randrange(0, 100, 9)  # 产生一个整形的数值
# print(b)
c = random.randint(1, 10)
# print(c)
li = [3, "ad", 45, "hh", "uil"]
d = random.choice(li)   # 随机选择内容
# print(d)

# random.shuffle() 打乱顺序

e = random.randint(65,90)
print(chr(e))
f = random.randint(97,122)
print(chr(f))
# print(ord('e'))
# print(ord('K'))

# hashlib模块
# 加密算法 md5、sha1、sha256
password = "88569698"
md5 = hashlib.md5(password.encode("UTF-8"))
print(md5.hexdigest())


sha1 = hashlib.sha1(password.encode("UTF-8"))
print(sha1.hexdigest())

sha256 = hashlib.sha256(password.encode("UTF-8"))
print(sha256.hexdigest())

# requests 模块
response = requests.get('https://www.csdn.net/')
# print(response.text)