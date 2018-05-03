# 管理员类
class Manager:
    menu = {
        '创建讲师账号':'','学生账号':'','创建课程':'','创建班级':''
    }
    def __init__(self,name):
        self.name = name

    def creatTeacher(self):
        # 输入讲师的姓名
        # 输入讲师的密码
        # 将讲师的信息写入userinfo文件
        # 输入：
            # 讲师所在的学校
        # 实例化一个讲师对象，存储在讲师对应的文件中
        pass

    def creatStudent(self):
        # 输入讲师的姓名
        # 输入讲师的密码
        # 将讲师的信息写入userinfo文件
        pass

    def createCourse(self):
        # 输入
        # 学科名称
        # 价格
        # 周期
        # 创建一个课程对象，dump进course文件

        pass

    def showCourse(self):
        # 打开文件
        # 将文件中的学科对象读出来，展示
        pass

    def createClasses(self):
        # 输入：
        # 班级名称、学校
        # 绑定一个学科对象，要先调用查看学科方法获取学科对象，用户选择学科，再将对象绑定到班级
        # 创建一个属于这个班级的文件用于存储学生信息，将文件的路径存储到班级对象中
        # 创建一个班级对象（名称 学校 学科对象 讲师空列表 学生信息所在文件的路径），dump进classes文件
        pass

    def showClasses(self):
        # 打开文件
        # 将文件中的班级对象读出来，展示
        pass

    def createStudent(self):
        # 输入：
        # 学生姓名，密码
        # 将学生信息写入userinfo文件中
        # 创建一个学生对象(姓名 讲师空列表)
        pass

    def boundClass(self):
        # 管理员选择为老师还是学生指定班级
        # 如果是为老师绑定班级：
            # 找到指定的老师和对应的班级（都是通过show方法查看之后选择）
            # 给讲师对象的班级属性的列表中加入一个新的项 ，值为班级的对象
            # 给班级对象中的讲师属性列表加入一个新的项，值为讲师的对象
        # 如果为学生绑定班级
            # 找到指定的学生和对应的班级（都是通过show方法查看之后选择）
            # 给学生创建新的班级属性，将属性的值设置为班级对象
            # 将学生对象的信息 根据班级对象中存储的学生信息存储路径 dump入对应文件
        pass


