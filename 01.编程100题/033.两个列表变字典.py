a = ['a', 'b', 'c']
b = [1, 2, 3]
d = {}

# 常规遍历方法
for i, j in zip(a ,b):
    d[i] = j
print(d)
# 直接zip + dict

new_dict = dict(zip(a, b))
print(new_dict)

# 转化为字典之后可以做排序/ 根据键来获取值

# 简单排个序
lst = [
    {"score": "张三", "socre": 66},
    {"score": "李四", "socre": 88},
    {"score": "王五", "socre": 90},
    {"score": "王五", "socre": 56},
]

new = sorted(new_dict,key = lambda x:x['score'])
print(new)