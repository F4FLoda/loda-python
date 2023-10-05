# 模块：把功能相近的函数或者类放在一个文件中，就称为模块，使用import导入
# 1.import 模块名
# 2.from 模块名 import 类名(函数名)/变量
# 3.from 模块名 import * 代表将此模块的所有内容全部导入

import math
import pyautogui
import pandas as pd
import sys
import time
import datetime

# 包：package，一个包里面存放多个模块，按照功能划分
# 包：存放py文件
# from 包 import 模块
# from 包.模块 import 类/函数/变量

from article import func

print(sys.path)
# print(sys.version)
# print(sys.argv)
# print(sys.maxsize)
# print(sys.base_prefix)
# print(sys.builtin_module_names)

# time模块
time.sleep(1)
t = time.time()
print(t)
# 将时间转换成字符串的形式
print(time.ctime(t))

# 将时间转换成元组的形式
t = time.localtime(t)
print(t)
print(t.tm_mon)

# 将元组时间转换成字符串的形式
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# datetime模块
print(datetime.date.today())
time_del = datetime.timedelta(days=3,hours=3)
now = datetime.datetime.now()                   # 当前时间
print(now)
result = now + time_del
print(result)
