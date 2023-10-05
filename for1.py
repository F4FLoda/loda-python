
# for...else案例：
for i in range(3):
    username = input("username:")
    password = input("password:")
    if username == "admin" and password == "123456":
        print("登录成功")
        break
    print("输入错误")
else:
    print("账户被锁定！")