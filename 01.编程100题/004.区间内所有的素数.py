From = int(input("起始"))
To = int(input("结束"))

# for i in range(From, To+1):
#     if i >1:
#         for j in range(2, To):
#             if i % j == 0:
#                 break
#         else:
#             print(i)

for num in range(From, To + 1):  # 创建从 1-100 的序列
    if num > 1:
        for i in range(2, num):  # 创建2-num的序列
            if num % i == 0:  # 取余为0则不为整数
                break
        else:
            print(num)

# 只可以被自身整除和1
# 判断一个数 是否是素数

# s = int(input("请输入一个正整数："))  # 11

# 注意是整除 所以不能比本身大 所以循环只需要本身即可

# if s < 2:
#     print("这个数不是素数！")
# elif s == 2:
#     print("这个是素数")
# else:
#     for i in range(2, s):
#         if s % i == 0:
#             print("这个数不是素数！")
#             break
#     else:
#         print("这个数是素数！")
