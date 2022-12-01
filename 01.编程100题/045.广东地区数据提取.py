"""
读取电话数据
import pandas as pd
df = pd.read_excel("面试成员电话号码.xlsx")
"""

"""
for i in df['电话']:
    nums.append(str(i))
print(nums)
"""
#
# data_prov_city = [(i, random.randint(2, 10)) for i in prov_city]
# print(data_prov_city)

"""
将数据封装成这样一个元组才能展示
[('珠海市', 人数), ('汕头市', 0), ('佛山市', 0), ('韶关市', 0), ...
"""

prov_city = ['珠海市', '汕头市', '佛山市', '韶关市',
             '湛江市', '肇庆市', '江门市', '茂名市',
             '惠州市', '梅州市', '汕尾市', '河源市',
             '阳江市', '清远市', '东莞市', '中山市',
             '潮州市', '揭阳市', '云浮市', '广州市', '深圳市']

import requests
import json

res = []
nums = ['18529389283', '13112861564', '18319717364', '13501509001', '13160808247', '18148669780', '13046138848',
        '18100263217', '19876224718', '15989844472', '19355372518', '14718067353', '13435500574', '15815096965',
        '17841718418', '13434238138', '16782450290', '13425228186', '19126600323', '13724633181', '19896825184',
        '15724146220', '15361356362', '13413537553', '13417086422', '13719560861', '18719356954', '13668998469',
        '18219102847', '13376535205', '17879554219', '18823507026', '15728282661', '13790701146', '18198430039',
        '18946968471', '13202470918', '17880683198', '18312595570', '13286556022', '14760437740', '15220665519',
        '18927801939', '13680567879', '13533112180', '18475268786', '17666251120', '17384679196', '18476708479',
        '19124697389', '18038588912', '13902503168', '15112911906', '15875279867', '18319868252', '13632399426',
        '15171546719', '18026260531']


def get_address(num: str):
    """
    传入手机号码-> 获取到对应的地址信息 -> 添加到res列表中
    :return:None
    """
    global res
    url = "https://eolink.o.apispace.com/phone/api/v1/forward/china/phone/attribution"
    payload = {"phone_number": num}
    # 定制请求头
    headers = {
        "X-APISpace-Token": "dw0w3vb3p5kbx1ejg4xmtc6tk27upuxp",
        "Authorization-Type": "apikey"
    }
    response = requests.request("GET", url, params=payload, headers=headers)
    # 将json数据转化为字典 便于提取
    datadict = json.loads(response.text)
    if datadict['data']['city'] + "市" in prov_city:
        res.append(datadict['data']['city'] + "市")

for i in range(len(nums)):
    get_address(nums[i])
print(res)

# 统计地区 类似 {'广州':8}
region_count = {}
for like in res:
    if like not in region_count:
        region_count[like] = 0
    region_count[like] += 1

