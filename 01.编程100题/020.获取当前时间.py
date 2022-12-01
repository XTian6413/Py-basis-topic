import datetime

curr_datatime = datetime.datetime.now()

print(curr_datatime)

str_time = curr_datatime.strftime("%Y-%m-%d %H:%M:%S")
print('str_time', str_time)
print("year:", curr_datatime.year)
print('month:', curr_datatime.month)
print('day:', curr_datatime.day)
print('hour:', curr_datatime.hour)
print('minute:', curr_datatime.minute)
print('second:', curr_datatime.second)

hour = input("请输入点数")
minute = input("请输入分钟")


while True:
    # 时刻获取当前时间
    curr_datatime = datetime.datetime.now()
    if hour == str(curr_datatime.hour) and minute == str(curr_datatime.minute):
        print("起床了")
        break
    else:
        print(curr_datatime.hour, curr_datatime.minute)
