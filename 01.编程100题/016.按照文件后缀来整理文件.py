# 小知识: 怎么获取文件后缀名
# import os
# data_name = os.path.splitext('016.按照文件后缀来整理文件.py')
# 获得元组(文件名,后缀) 要第2个并把 .去除
# print(data_name[1][1:])

# 小知识
import shutil
# shutil.move('文件1','文件夹2') # 将文件1移动到文件夹下面


import os
import shutil
dir = "../arrange_dir"

for fileName in os.listdir(dir):
    ext = os.path.splitext(fileName)[1][1:]
    print(ext)
    if not os.path.isdir(f'{dir}/{ext}'):
        os.mkdir(f'{dir}/{ext}')

    source_path = f"{dir}/{fileName}"
    target_path = f"{dir}/{ext}/{fileName}"
    shutil.move(source_path,target_path)