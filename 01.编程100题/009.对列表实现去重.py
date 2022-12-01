lst = [1, 1, 2, 2, 3, 4, 5, 5, 6, 6, 6, 6, 6, 6]
print(len(lst))
# print(list(set(lst)))


List = [3,3,2,4,4,5]
NewList = []
for id in List:
    if id not in NewList:
        NewList.append(id)
print (NewList)

#结果：[3, 2, 4, 5]