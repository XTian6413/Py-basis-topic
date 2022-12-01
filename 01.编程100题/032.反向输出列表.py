# 方法一 切片操作
list1 = [1, 2, 3, 4, 5, 6]
list1 = list1[::-1]
print(list1)

list1 = [1, 2, 3, 4, 5, 6]
# 方法二反向遍历
print("[", end="")
for i in range(len(list1), 0, -1):
    if i == len(list1) - 5:
        print(i, end="")
    else:
        print(i, end=", ")
print("]", end="")
print()
# 双指针
list1 = [1, 2, 3, 4, 5, 6]
i = 0
j = len(list1) - 1
while i < j:
    temp = list1[i]
    list1[i] = list[j]
    list1[j] = temp
    i += 1
    j -= 1
print(list1)

#
# l1 = [1,2,4], l2 = [1,3,4]
# [1,1,2,3,4,4]

l1 = [1, 2, 4]
l2 = [1, 3, 4]

for i in l1:
    l2.append(i)
l2.sort()
print(l2)
