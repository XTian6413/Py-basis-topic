list1 = [1, 2, 3, 4, 5, 6]
print(sum(list1))

# 不适用sum

sum = 0
for i in list1:
    sum += i

print(sum)

# 使用len函数
sum = 0
for i in range(len(list1)):
    sum += list1[i]
print(sum)

# 排序
for i in range(len(list1)-1):
    for j in range(len(list1)-1-i):
        if list1[j] < list1[j+1]:
            list1[j] ,list1[j + 1] = list1[j + 1],list1[j]
print(list1)