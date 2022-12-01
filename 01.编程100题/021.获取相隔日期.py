import datetime

birthday = "2004-11-18"
# birthday = input("请输入你的出生的日期,格式为(2000-01-01)")
birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")  # 将字符串转化为datatime对象
curr_datetime = datetime.datetime.now()  # 获取到当前时间

minus_datetime = curr_datetime - birthday_date
print(f"你一共活了{minus_datetime.days}天")
print(f'你已经是{minus_datetime.days/365}岁了')
month = datetime.datetime.now().month
day = datetime.datetime.now().day


if str(month) == birthday[5:7] and str(day) == birthday[8:10]:
    print('另外,祝你生日快乐♡ ☺')