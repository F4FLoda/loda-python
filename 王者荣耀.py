import time

# import random

# 存放所有角色的list
all_role = []
while True:
    choice = input("请选择：1.添加角色\n 2.删除角色\n 3.修改角色\n 4.查询角色\n 5.显示所有角色\n 6.退出系统\n")
    # 判断
    if choice == '1':
        print("添加角色模块：\n")
        name = input("\t名称：")
        sex = input("\t性别：")
        job = input("\t职业：")
        role = [name, sex, job]
        all_role.append(role)
    elif choice == '2':
        print("删除角色：\n")
        role_name = input("输入名称：")
        for role in all_role:
            if role_name in role:
                all_role.remove(role)
                print("成功删除:{}".format(role_name))
                break
            else:
                print("不存在此角色，请重新输入：")
    elif choice == '3':
        pass
    elif choice == '4':
        print("查询角色：\n")
        role_name = input("输入名称：")
        for role in all_role:
            if role_name in role:
                print("{}{}{}".format(role[0].ljust(30), role[1].ljust(30), role[2].ljust(30)))
                break
            else:
                print("不存在此角色，请重新输入：")
    elif choice == '5':
        print("显示所有角色：\n")
        for role in all_role:
            print(role[0].center(10), end=" ")
            print("\n")
            print(role[1].center(10), end=" ")
            print("\n")
            print(role[2].center(10), end=" ")
            print("\n")
    elif choice == '6':
        print("正在退出系统...")
        time.sleep(3)
        print("成功推出！")
    else:
        print("输入错误，请重新选择！")
