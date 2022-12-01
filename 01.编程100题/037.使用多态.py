class Animal:  # 抽象类(接口)
    def speak(self):  # 抽象方法 空实现的 -> pass
        pass  # 确定父类有哪些方法(定义一个标准)  再 由子类来实现
class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

# 定义一个函数来制作噪音  传入animal对象
def make_noise(animal:Animal):
    animal.speak()

# 演示多态

# 同样的行为 使用不同的对象 获得不用的运行状态
dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)