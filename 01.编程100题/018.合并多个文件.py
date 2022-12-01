import os
contents = []
data_dir_path = 'D:\小小项目\编程题目\many_text'
for file in os.listdir(data_dir_path):
    file_path = f'{data_dir_path}/{file}'
    if os.path.isfile(file_path) and file.endswith('.txt'):   # 判断某一对象(需提供绝对路径)是否为文件
        with open(file_path, encoding="utf-8") as fin:
            contents.append(fin.read())

final_content = "\n".join(contents)  # 每个内容通过换行符来分割
print(final_content)
with open('018.all_text.txt',mode='w',encoding="utf-8") as f:
    f.write(final_content)

"""
==============================拓展==========================
save_path为输入的保存路径。
意思是输入路径若为文件，提示保存路径应该为目录。输入路径不存在，创建目录。
save_path = ''
if os.path.isfile(save_path):
    raise RuntimeError('the save path should be a dir')
if not os.path.exists(save_path):
    os.mkdir(save_path)
"""

