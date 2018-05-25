# -*- encoding: utf-8 -*-
# @Time    : 2018-05-25 23:02
# @Author  : mike.liu
# @File    : logging模块.py
import logging
class IgnoreBackupLogFilter(logging.Filter):
    """忽略带db backup的日志"""
    def filter(self, record):   # 固定写法
        return "db backup" not in record.getMessage()


# console handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
fh = logging.FileHandler('mysql.log')



# formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger = logging.getLogger("Mysql")
logger.setLevel(logging.DEBUG)  # logger优先级高于其它输出途径的

# add handler to logger instance
logger.addHandler(ch)
logger.addHandler(fh)

# add filter
logger.addFilter(IgnoreBackupLogFilter())

logger.debug("test....")
logger.info("test info...")
logger.warning("start to run db backup job...")
logger.error("test error")