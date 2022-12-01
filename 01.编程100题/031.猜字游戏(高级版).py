import random
import time

guess_num = random.randint(1, 100)
count = 0
start = time.time()
while True:
    try:
        num = int(input("请输入你猜的数字: "))
        if num not in range(1, 101):
            print('只可以输入1-100的整数哦,请重新输入: ')
            continue
    except:
        print("只可以输入1-100的整数哦,请重新输入: ")
        continue
    count += 1
    if num < guess_num:
        print("小了")
        continue
    elif num > guess_num:
        print("大了")
        continue
    else:
        print("恭喜你猜对了")
        break
end = time.time()
if count <= 5:
    print(f"超越神啦,你一共用了{count}次")
elif count <= 7:
    print(f"杀敌如麻,你一共用了{count}")
else:
    print(f"智商余额不足,请及时充值,你一共用了{count}次")
print(f"一共用时: {round(end - start,1)}秒")
