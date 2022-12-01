# 两个数做比较 如果后面的数比前面的大 就交换位置 -> 使用python语言特性 a, b = b, a

nums = [5, 8, 1, 54, 87, 50, 36]

# 直接排序
# nums.sort()
# print(nums)

"""
0 1 2 3 4 5
0 1 2 4 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1
"""
for i in range(len(nums) - 1):
    for j in range(len(nums) - 1 -i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)

# 