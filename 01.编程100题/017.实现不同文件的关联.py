# 先读取老师课程信息
tea_dict = {}
with open("017.course_teachers",'r',encoding='utf-8') as tf:
    for i in tf.readlines():
        i.replace("\n", "")
        tea_dict[i[:2]] = i[3:6]
# 或者直接  科目, 老师姓名 = split(",") 然后赋值给字典 tea_dict[科目] = 老师姓名
print(tea_dict)

# 读取学生信息
with open('017.students_grade.txt','r',encoding='utf-8') as sf:
    for i in sf.readlines():
        course, num, name, score = i.replace("\n","").split(",")
        # 使用字典的get方法取值
        teacher = tea_dict[course]
        print(course,teacher,name,score)
    # 要求输出格式: ['语文', 老师名字, '101', '小张', '94']

