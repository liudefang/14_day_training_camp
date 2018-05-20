# -*- encoding: utf-8 -*-
# @Time    : 2018-05-20 17:43
# @Author  : mike.liu
# @File    : logics.py
from 作业.第五次作业.ATM.atm.transaction import make_transaction


def view_account_info(account_data, *args, **kwargs):
    """查看账号信息"""
    trans_logger = kwargs.get("transaction_logger")
    print("ACCOUNT INFO".center(50, '-'))
    for k, v in account_data['data'].items():
        if k not in ('password',):
            print("%15s: %s" %(k, v))
    print("END".center(50, '-'))


def with_draw(account_data, *args, **kwargs)
    # 取现
    trans_logger = kwargs.get("transaction_logger")
    current_balance = '''----------- BALANCE INFO ---------
        Credit :    %s
        Balance:    %s''' % (account_data['data']['credit'], account_data['data']['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("\033[33;1m请输入取现金额:\033[0m").strip()
        if len(withdraw_amount) > 0 and withdraw_amount.isdigit():
            withdraw_amount = int(withdraw_amount)
            if (account_data['data']['balance'] /2 ) >= withdraw_amount:
                transaction_result = make_transaction(trans_logger, account_data, 'withdraw', withdraw_amount)
                if transaction_result['status'] == 0:
                    print('''\033[42;1m您的余额:%s\033[0m''' % (account_data['data']['balance']))
                else:
                    print(transaction_result)
            else:
                print_warning("可取现余额不足,可提现%s:" %(int(account_data['data']['balance'] / 2)))

        if withdraw_amount == 'b':
            back_flag = True
