import requests
import json
import pandas as pd

# 定义在外面 -> 因为两个函数都需要用到
res = []
df = pd.read_excel("info.xlsx", converters={'电话': str})  # 指定字符串为str类型


def add_info():
    """
    获取到每一位学生的手机号码
    若手机号码为空则赋值为: 电话号码缺失
    :return:  手机号码的列表
    """
    global df
    tel_num = df['电话']
    tel_num_list = []
    for i in tel_num:
        i = str(i)
        if i == "nan":
            i = "电话号码缺失"
        tel_num_list.append(i)
    return tel_num_list


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
    # 将省份和城市添加到列表中
    try:
        datadict = json.loads(response.text)
        res.append(datadict['data']['province'] + datadict['data']['city'])
    except Exception as e:
        print(f"第{i}条数据有误, 请手动解决,出现的问题为: {e}, 错误信息为: {datadict}")
        res.append("数据有误")

def modify_class():
    """
    将数字全部转化为小写的
    :return: None
    """
    Class = df["班级"]
    new_Class_test = []
    for i in Class:
        i = str(i)
        i = i.replace("一", "1").replace("二", "2").replace("三", "3"). \
            replace("四", "4").replace("五", "5").replace("六", "6").replace("七", "7").replace("计科", "计算机科学与技术")
        new_Class_test.append(i)
    df["班级"] = new_Class_test

def save_excel():
    """
    新增一列号码归属地并将地址赋值给该列
    :return: None
    """
    df['号码归属地'] = res
    # 保存并去除前面的数字列
    df.to_excel('修改后的teseData文件.xlsx', index=False)


if __name__ == '__main__':
    print("\033[31m========程序开始执行==========\033[0m")

    # 接收到手机号码和缺失号码对应的索引
    tel_num_list = add_info()
    for i in tel_num_list:
        if i == "电话号码缺失":
            print(f"\033[31m索引为:{tel_num_list.index(i)}的手机号码缺失\033[0m")
            res.append("电话号码缺失")
            print(res)
        else:
            get_address(i)
            print(res)
    # 获取到归属地数据之后添加并保存到excel表格中
    save_excel()
