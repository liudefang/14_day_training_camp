# -*- encoding: utf-8 -*-
# @Time    : 2018-05-20 15:38
# @Author  : mike.liu
# @File    : main.py
from 作业.第五次作业.ATM.atm import logics
from 作业.第五次作业.ATM.atm.auth import authenticate
from 作业.第五次作业.ATM.atm.logger import logger

transaction_logger = logger("transaction")
access_logger = logger("access")

features = [
    ('账号信息', logics.view_account_info),
    #('取现', logics.with_draw),
    #('还款', logics.pay_back),
]

def controller(user_obj):
    """功能分配"""
    while True:
        for index, feature in enumerate(features):
            print(index, feature[0])
        choice = input("请选择进行相应的功能:").strip()
        if not choice:
            continue
        if choice.isdigit():
            choice = int(choice)
            if 0<= choice < len(features):
                features[choice][1](user_obj, transaction_logger = transaction_logger, access_logger = access_logger)
            if choice == 'q':
                exit('退出成功...')
def entrance():
    '''ATM程序入口'''

    user_obj = {
        'is_authenticated': False, # 用户是否已认证
        'data': None
    }

    retry_count = 0
    while user_obj['is_authenticated'] is not True: # 没认证
        username = input("\033[32;1m输入用户名:\033[0m").strip()
        password = input("\033[32;1m输入密码:\033[0m").strip()
        auth_data = authenticate(username, password)    # 验证
        # 拿到账号数据auth_data
        if auth_data:
            user_obj['is_authenticated'] = True
            user_obj['data'] = auth_data
            print('欢迎登录成功,%s' % username)
            access_logger.info('用户%s正常登录' %user_obj['data']['id'])
            controller(user_obj)

        else:
            print("输入的用户名或密码错误,请重新输入!")
        retry_count += 1
        if retry_count == 3:
            msg = "用户%s的密码输错了3次,请稍后再试!"
            print_error(msg)
            access_logger.info(msg)
            break
