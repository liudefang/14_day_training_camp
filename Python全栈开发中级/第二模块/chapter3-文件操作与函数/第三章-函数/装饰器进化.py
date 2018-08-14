# -*- encoding: utf-8 -*-
# @Time    : 18-5-16 上午9:53
# @Author  : mike.liu
# @File    : 装饰器进化.py

user_status = False
def login(auth_type):  # 把要执行的模块从这里传进来
    def auth(func):


        def inner(*args, **kwargs):  # 再定义一层函数
            if auth_type == 'qq':
                _username = 'mike'
                _password = '123'
                global user_status

                if user_status == False:
                    username = input('请输入用户名:').strip()
                    password = input('请输入密码:').strip()

                    if username == _username and password == _password:
                        print('欢迎登录成功, %s' % username)
                        user_status = True

                    else:
                        print('输入的用户名或密码错误！')

                if user_status == True:
                    func(*args, **kwargs)  # 看这里看这里，只要验证通过了，就调用相应功能
            else:
                print('只能qq登录')

        return inner # 用户调用login时，只会返回inner的内存地址，下次再调用时加上（）才会执行inner函数
    return auth


def home():
    print('首页'.center(20, '-'))

@login('qq')
def america():
    # login()   # 执行前加上验证
    print('欧美专区'.center(20, '-'))


def japan():
    print('日韩专区'.center(20, '-'))

@login('weibo')
def henan(style):
    '''
    :param style: 喜欢看什么节目，就传进来
    :return:
    '''
    # login()   # 执行前加上验证
    print('湖南专区'.center(20, '-'))

home()
henan = login(henan)

america()

henan('快乐大本营')