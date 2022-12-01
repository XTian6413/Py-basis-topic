lst = [1, 2, 3, 4, 5, 6]
lst1 = [5, 6]

for i in range(len(lst1), -1, -1):
    if i in lst:
        lst.remove(i)
print(lst)
# lst = [1, 2, 3, 4, 5, 6]
# lst1 = [5, 6]
# lst = [i for i in lst if i not in lst1]
# print(lst)

