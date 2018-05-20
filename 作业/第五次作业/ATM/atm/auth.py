# -*- encoding: utf-8 -*-
# @Time    : 2018-05-20 16:50
# @Author  : mike.liu
# @File    : auth.py
from 作业.第五次作业.ATM.atm.db_handler import load_account_data


def authenticate(username, password):
    """对用户信息进行验证"""
    account_data = load_account_data(username)
    if account_data['status'] == 0:     # 账号文件加载成功
        account_data = account_data['data']     # 用户数据
        if password == account_data['password']:    # 判断密码是否正确
            return account_data
        else:
            return None
    else:
        return None