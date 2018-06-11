# -*- encoding: utf-8 -*-
# @Time    : 18-6-11 上午11:02
# @Author  : mike.liu
# @File    : start.py
from 第七次作业.FTP.ftpserver.core.ftpserver import create_db, create_dir, settings
from 第七次作业.FTP.ftpserver.modules import sokect_server

# 创建用户数据库文件和宿主目录


if __name__ == "__main__":
    create_db()
    create_dir()

    server = sokect_server.socketserver.ThreadingTCPServer(settings.IP_PORT, sokect_server.Myserver)
    server.serve_forever()
