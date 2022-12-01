# 列表的排序
# 将列表的最大值和最小值 放在头和尾 其余元素不变
# 不适用max()和min()函数
lst = [5, 4, 3, 2, 1, 6]

# 不使用sort时
max = lst[0]
min = lst[0]

for i in range(len(lst)-1,-1,-1):
    if max < lst[i]:
        max = lst[i]
else:
    lst.remove(max)
    lst.insert(0, max)
print(lst)
# for i in range(len(lst)):
#     if min > lst[i]:
#         min = lst[i]
# else:
#     lst.remove(min)
#     lst.insert(-1, min)
# print(lst)
