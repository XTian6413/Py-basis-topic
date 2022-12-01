a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100]  # 原始列表
# 插入的数字为7
# a = [1, 4, 7, 6, 9, 13, 16, 19, 28, 40, 100]
num = 41
for i in range(len(a)):
    if num < a[i]:
        a.insert(i, num)
        break
print(a)