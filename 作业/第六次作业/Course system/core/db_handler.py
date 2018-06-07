# -*- encoding: utf-8 -*-
# @Time    : 2018-06-06 22:07
# @Author  : mike.liu
# @File    : db_handler.py

'''处理与数据之间的交互，如果file_db_storage，返回路径'''
import os
import pickle


def db_handler(conn_parms):
    if conn_parms['engine'] == 'file_storage':
        return file_db_handle(conn_parms)

def file_db_handle(conn_parms):
    '''
    对文件路径做语法分析
    :param conn_parms:
    :return:
    '''
    db_path = '%s/%s'%(conn_parms['path'], conn_parms['name'])
    return db_path
