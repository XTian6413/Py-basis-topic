# 输出7行的菱形
"""
    * 1      4
   *** 3     3
  ***** 5    2
 ******* 7   1
********* 9  0
 ******* 7   1
  ***** 5    2
   *** 3     3
    * 1      4
"""

# 一共有九行 菱形的边长为5
# 因为是菱形 所以是2n-1行


line = 9
# lst = [1, 3, 5, 7, 9]
# lst2 = [7, 5, 3, 1]
# count = 4
# for i in lst:
#     # 输出空格
#     print(" "*count, end="")
#     print("*"*i)
#     count -= 1
#
# count2 = 1
# for i in lst2:
#     print(" "*count2,end="")
#     print("*"*i)
#     count2 += 1

a = line // 2
print(a)# 连个4行 + 1行
