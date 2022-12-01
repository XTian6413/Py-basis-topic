import os
# 获取单个文件的大小
print(os.path.getsize("012.信息.txt"), "字节")
print()
Sum = 0
for fileName in os.listdir(""):
    # 获取到所有文件的e名称
    datasiez = os.path.getsize("./"+fileName)
    print(fileName, datasiez)
    Sum += datasiez
print(Sum)

import shutil
shutil.move('要移动的文件','指定文件夹下')