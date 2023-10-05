import random

nums = []
for a in range(10):
    ran = random.randint(1, 100)
    nums.append(ran)
# 冒泡排序
for i in range(0, len(nums) - 1):
    for j in range(0, len(nums) - 1 - i):
        if nums[j] > nums[j + 1]:
            # 交换方法1：
            # tmp = nums[j]
            # nums[j] = nums[j + 1]
            # nums[j + 1] = tmp

            # 交换方法2：
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)
