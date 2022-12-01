# 方法一 第三方变量
# a = 1
# b = 2
# -------------
# c = a
# a = b
# b = c
# print(a)
# print(b)
# 方法二 加减法
# a = a + b
# b = a - b
# a = a - b
# print(a)
# print(b)
# 方法三 语言特征 元组
# a, b = b, a
# print(a)
# print(b)
# 方法四 按位异或
# a = a ^ a ^ b
# print(a)
# a = 1
# b = b ^ b ^ a
# print(b)

# 使用按位异或来找出列表的单个的值

nums = [2, 2, 1]
re = 0  # 0异或任何数都是任何数
for i in nums:
    re = re ^ i
print(re)
