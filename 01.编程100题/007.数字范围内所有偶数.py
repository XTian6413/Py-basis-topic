# 输出范围内所有的偶数

From = int(input("From:"))
To = int(input("To:"))

# for i in range(From, To + 1):
#     if i %2 == 0:
#         print(i)

data = [i for i in range(From, To + 1) if i %2 == 0]
print(data)