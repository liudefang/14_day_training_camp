# -*- encoding: utf-8 -*-
# @Time    : 18-6-9 下午2:29
# @Author  : mike.liu
# @File    : ftptest.py
import logging
import os

from 第七次作业.FTP.ftpserver.conf import settings

for username in settings.USERS_PWD:
   # user_home_path = settings.HOME_PATH + r"/%s" % username
    user_home_path = "/home/mikeliu/python/14_day_training_camp/作业/第七次作业/FTP/ftpserver/home/jack"
    #print(user_home_path)
    if os.path.isdir(user_home_path):

        logging.info("目录已经存在")
        #print("目录已经存在")
    else:
        os.makedirs(user_home_path)
        #print("创建用户宿主目录【%s】成功!" % user_home_path)


