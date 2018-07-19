# -*- encoding: utf-8 -*-
# @Time    : 18-5-23 上午9:18
# @Author  : mike.liu
# @File    : os.py
import os
print(os.getcwd)  # 得到当前工作目录，即当前Python脚步工作的目录路径
print(os.listdir())     # 返回指定目录下的所有文件和目录名
# print(os.remove())      # 删除一个文件
# print(os.removedirs(r"/home/第九次作业"))
# print(os.system())      # 运行shell命令
print(os.environ)       # 返回操作系统所有的环境变量
print(os.getenv("home"))    # 读取操作系统环境变量HOME的值
print(os.environ.setdefault('HOME', '/home/mikeliu'))   # 设置系统环境变量，仅程序运行有效
print(os.linesep)   # 给出当前平台使用的行终止符
print(os.name)      # 指示你正在使用的平台
print(os.rename())  # 重命名
print(os.makedirs(r"/opt/第九次作业"))        # 创建多个目录
print(os.mkdir())       # 创建单个目录
print(os.stat())        # 获取文件属性
print(os.chmod())   # 修改文件权限和时间戳
print(os.chdir(dirname))   # 改变工作目录到dirname
print(os.kill(10885, signal.SIGKILL))

print(os.path.isfile())     # 检验给出的路径是否是一个文件
print(os.path.isdir())      # 检验给出的路径是否是一个目录
print(os.path.isabs())      # 判断是否是绝对路径
print(os.path.exists())     # 检验给出的路径是否真的存在
print(os.path.split('/opt/ddt-1.1.3.tar.gz'))       # 返回一个路径的目录名和文件名
print(os.path.splitext('/opt/ddt-1.1.3.tar.gz'))        # 分离扩展名
print(os.path.dirname())        # 获取路径名
print(os.path.abspath())        # 获取绝对路径
print(os.path.basename())       # 获取文件名
print(os.path.getsize())        # 获取文件大小
print(os.path.join(dir, filename))       # 结合目录名与文件名


