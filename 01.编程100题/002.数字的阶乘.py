def jiecheng(n):
     result = 0
     while n > 0:
         result *= n
     return result

n = int(input("n:"))
print(f"{n}的阶乘为",jiecheng(n))

n = int(input("n:"))
result = 1
while n > 0:
    result *= n
    n -=1
print(result)
