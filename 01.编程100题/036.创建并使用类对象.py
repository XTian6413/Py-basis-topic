# 定义一个标准的手机类
class Phone:
    def __init__(self, name, price, mode):
        # 手机通用特点(共享)
        self.name = name
        self.price = price
        self.mode = mode

    def use_phone(self):
        print(f"{self.name}正在使用中价格为:{self.price},现在手机运行的模式为:{self.mode}")

    def close_phone(self):
        print(f"{self.name}手机关机了")

    def open_phone(self, open_time):
        print(f"此次数开机的时间为{open_time}")

# 创建一个对象
my_phone = Phone("苹果", 8999, "14Plus")
# 使用 使用手机方法
my_phone.use_phone()
# 使用 关机方法
my_phone.open_phone(10)

# 继承一下 Phone的类
class IPhone(Phone):
    # 演示重写
    def use_phone(self):
        # 我认为不够好 所以我要重写
        print("重写iPhone的方法")
    # 自己新增一个方法
    def face_id(self):
        print("人脸识别成功")
        print("Hello")
