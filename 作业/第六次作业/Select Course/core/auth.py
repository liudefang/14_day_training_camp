# -*- encoding: utf-8 -*-
# @Time    : 2018-06-06 21:27
# @Author  : mike.liu
# @File    : auth.py
from core import accounts

# 用户认证


def access_login(user_data, log_obj):
    '''
    登录函数，当登录失败超过三次，则退出
    登录成功之后，查看个人的身份，来确定进入哪个视图
    :param user_data:
    :param log_obj:
    :return:
    '''

    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3:
        account = input("\033[33;1m;请输入管理员用户名:\033[0m".center(20, '-')).strip()
        password = input("\033[33;1m;请输入管理员密码:\033[0m".center(20, '-')).strip()
        # 用户账号密码正确，则返回用户数据的字典
        auth = access_auth(account, password, log_obj)
        if auth:
            user_data['is_authenticated'] = True    # 用户认证为True
            user_data['account_id'] = account   # 用户账号ID为账号名
            return auth
        else:
            print("用户[%s]错误次数太多，请稍后再试!" % account)
            log_obj.error("用户[%s]错误次数太多，请稍后再试!" % account)
            exit()


def access_auth(account, password, log_obj):
    '''
    下面access_login调用access_auth方法，用户登录
    :param account: 用户名
    :param password: 密码
    :param log_obj:
    :return:
    '''
    account_data = accounts.MyPickle.load_account(account)
    if account_data['is_authenticated']:
        if account_data['vip_password'] == password:
            log_obj.info("欢迎【%s】登录成功" % account)
            return account_data
        else:
            log_obj.error("用户名或密码错误!")
            print("\033[31;1m用户名或密码错误!\033[0m")
    else:
        log_obj.error("用户名不存在!")
        print("用户名不存在!")
