# 方法一: 逆向遍历
lst = [1, 2, 3, 4, 5, 6]
lst1 = [5, 6]

for i in range(len(lst1), -1, -1):
    if i in lst:
        lst.remove(i)
print(lst)

# 方法二: 列表生成式+判断
lst = [1, 2, 3, 4, 5, 6]
lst1 = [5, 6]
lst2 = [i for i in lst if i not in lst1]
print(lst)

