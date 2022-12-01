lst = [1, 1, 2, 2, 3, 4, 5, 5, 6, 6, 6, 6, 6, 6]
# 直接使用set函数 转化为集合(集合不能有重复元素)
print(list(set(lst)))
#结果：[1,2,3,4,5,6]

List = [3,3,2,4,4,5]
NewList = []
for id in List:
    if id not in NewList:
        NewList.append(id)
print (NewList)

#结果：[3, 2, 4, 5]
