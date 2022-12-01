import string

# 方法一使用string模块
# def test1():
#     lowercase = string.ascii_lowercase
#     uppercase = string.ascii_uppercase
#     print(lowercase)
#     print(uppercase)

# 方法二 chr转换
# def test2():
#     for i in range(65, 91):  # range(97,122) 是小写的字母
#         print(chr(i))
# test2()

# ====================================================
d = {}
# lowercase = string.ascii_lowercase
# index = 0
# for i in lowercase:
#     d[i] = str(index)
#     index += 1
# print(d)
#
# a = lowercase.startswith('a')
# print(a)

for i in range(97, 123):
    d[chr(i)] = str(i-97)
print(d)

for i in range(ord('a'), ord('z')+1):
    print(chr(i), end=" ")
for i in range(ord('A'), ord('Z')+1):
    print(chr(i), end=" ")

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        d = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9', 'k': '10', 'l': '11', 'm': '12', 'n': '13', 'o': '14', 'p': '15', 'q': '16', 'r': '17', 's': '18', 't': '19', 'u': '20', 'v': '21', 'w': '22', 'x': '23', 'y': '24', 'z': '25'}
        res1 = ""
        for i in firstWord:
            res1 = res1 + d[i]
        res2 = ""
        for i in secondWord:
            res2 = res2 + d[i]
        res3 = ""
        for i in targetWord:
            res3 = res3 + d[i]
        if res1.startswith('0'):
            res1.replace('0',"")
        if res2.startswith('0'):
            res2.replace('0',"")
        if res3.startswith('0'):
            res3.replace('0',"")
        return int(res1) + int(res2) == int(res3)