list1 = ['v', 'a', 'a', 'b', 'c', 'd', 'e']
# for i in list1:
#     print(i)
# print(len(list1))

# list2.remove("黄瓜")
# print(list2)
n = 0
while n < len(list1):
    if list1[n] == 'a':
        list1.remove('a')
    else:
        n += 1
print(list1)

list2 = ["黄瓜", "茄子", "白菜", "黄瓜", "黄瓜"]
for i in list2:
    if i == "黄瓜":
        list2.remove(i)
        list2.insert(2, 1)

list2[3] = "番茄"
print(list2)

index1 = list2.index("番茄")
print(index1)