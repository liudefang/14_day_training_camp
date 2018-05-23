# -*- encoding: utf-8 -*-
# @Time    : 2018-05-23 21:50
# @Author  : mike.liu
# @File    : shutil.py

import shutil
# shutil.copyfileobj(open('old'), open('new', 'w')) # 将文件内容拷贝到另一个文件中

#shutil.copyfile('f1.log', 'f2.log')     # 拷贝文件，目标文件无需存在

# shutil.copymode('f1.log', 'f2.log')    # 目标文件必须存在
#
# shutil.copystat('f1.log', 'f2.log')      # 目标文件必须存在

# shutil.copy('f1.log', 'f2.log')

# shutil.copy2('f1.log', 'f2.log')
# shutil.rmtree('folder1')    # 递归的去删除文件目录
# shutil.move('folder1', 'folder2')       # 移动文件夹，类似mv
# ret = shutil.make_archive('my_proj_bak', 'gztar', root_dir='my_proj')       #将 my_proj 下的文件打包放置当前程序目录

# zipfile压缩&解压缩
import zipfile
# z = zipfile.ZipFile('log.zip', 'w')
# z.write('f1.log')
# z.write('f2.log')
# z.close()

# z = zipfile.ZipFile('log.zip', 'r')
# z.extractall(path='.')
# z.close()
# 压缩为tar
import tarfile
t = tarfile.open('log.tar', 'w')
t.add('f1.log', arcname='f1.bak')
t.close()
