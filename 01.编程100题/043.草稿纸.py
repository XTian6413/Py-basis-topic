# 主要获取到 每个地区的人数就行了
# such as : [('清远市', 10), ('肇庆市', 7), ('深圳市', 2), ('广州市', 8)]
def get_data_tuple():
    prov_city = ['清远市', '肇庆市', '深圳市', '广州市']
    count = [10, 7, 2, 8]

    data_prov_city = [(i, j) for i, j in zip(prov_city, count)]
    print(data_prov_city)

    d = {'清远市': 10, '肇庆市': 7, '深圳市': 2, '广州市': 8}
    res = []
    for key in d:
        res.append((key, d.get(key)))
    print(res)


import random

prov_city = ['广州市', '深圳市',
             '珠海市', '汕头市', '佛山市', '韶关市',
             '湛江市', '肇庆市', '江门市', '茂名市',
             '惠州市', '梅州市', '汕尾市', '河源市',
             '阳江市', '清远市', '东莞市', '中山市',
             '潮州市', '揭阳市', '云浮市']

data_prov_city = [(i, random.randint(2, 10)) for i in prov_city]
print(data_prov_city)
data_prov_city = [('广州市', 6), ('深圳市', 2), ('珠海市', 6), ('汕头市', 4), ('佛山市', 9), ('韶关市', 9), ('湛江市', 7), ('肇庆市', 4), ('江门市', 8),
        ('茂名市', 6), ('惠州市', 2), ('梅州市', 8), ('汕尾市', 8), ('河源市', 8), ('阳江市', 5), ('清远市', 6), ('东莞市', 2), ('中山市', 5),
        ('潮州市', 7), ('揭阳市', 6), ('云浮市', 6)]

my_do = [('广州市', 8), ('东莞市', 2), ('梅州市', 5), ('佛山市', 5), ('汕尾市', 2), ('河源市', 3), ('汕头市', 5), ('潮州市', 3), ('清远市', 3),
                      ('湛江市', 3), ('茂名市', 3), ('中山市', 2), ('揭阳市', 2), ('惠州市', 3), ('肇庆市', 3), ('韶关市', 1), ('阳江市', 1)]
