# -*- encoding: utf-8 -*-
# @Time    : 2018-05-20 16:27
# @Author  : mike.liu
# @File    : db_handler.py
import os,json
from 作业.第五次作业.ATM.conf import settings


def load_account_data(account):
    '''根据account id 找到相应的账号文件，并加载'''

    account_file = os.path.join(settings.DB_PATH, "%s.json" % account)
    if os.path.isfile(account_file):
        f = open(account_file)
        data = json.load(f)
        f.close()
        return {'status': 0, 'data': data}
    else:
        return {'status': -1, 'error': '用户认证文件不存在!'}


