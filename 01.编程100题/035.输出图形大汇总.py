# 外层循环表示行 内层循环表示列
# 如下 : 三行四列
for i in range(3):
    for j in range(4):
        print("*",end="")  # 在同一行输出 并 不换行
    print()

print("===================")

# 输出三角形
for i in range(1, 6):
    for j in range(1, i+1):
        print("*",end="")  # *的个数与行数相同 range(1,2) range(1,3) range(1,4)
    print()

print("===================")

# 输出倒三角形
"""
i = 1 2 3 4 5 6
找到i与6 5 4 3 2 的关系 -> (1, 7-i)
***** range(1,6)
****  range(1,5)
***   range(1,4)
**    range(1,3)
*     range(1,2)
"""
for i in range(1,6):
    for i in range(1,7-i):
        print("*", end="")
    print()

print("===================")
"""

行号不变
i = 1 2 3 4 5 6
找到i与1, 3, 5, 7, 9的关系 -> 

输出一个等腰三角形  &(空格)
&&&&*       1    4 
&&&***      3    3
&&*****     5    2
&*******    7    1
*********   9    0

"""
for i in range(1,6):
    # 先输出一个倒三角形
    for j in range(1, 6 - i):
        print(" ", end="")
    # 在输出 1 3 5 7的三角形 range(1,2) range(1,4) range(1, 6) range(1,8) range(1,10)
    for k in range(1,i*2):
        print("*",end="")
    print()


