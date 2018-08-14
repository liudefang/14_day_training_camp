class Classes:
    def __init__(self,school,name,kind):
        self.school = school  # 学校
        self.name = name    # 班级名称 例如 python_s9
        self.kind = kind    # 班级科目 例如 python  go linux
        self.student = ['student_obj']

class Course:
    def __init__(self,name,period,price):
        self.name = name      # 课程名
        self.period = period  # 课程周期
        self.price = price    # 课程价格
c = Course('python','6 month',19800)

class Teacher:
    def __init__(self,name):
        self.name = name
        self.classes = ['classes_obj']
        # self.course = c    # 组合

t = Teacher('egon')
t.course = c    # 组合
# t.course.price