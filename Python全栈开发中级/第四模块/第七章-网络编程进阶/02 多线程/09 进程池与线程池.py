# -*- encoding: utf-8 -*-
# @Time    : 18-7-11 下午7:20
# @Author  : mike.liu
# @File    : 09 进程池与线程池.py

# 进程池
# from concurrent.futures import ProcessPoolExecutor
#
# import os, time, random
#
# def task(n):
#     print('%s is runing' % os.getpid())
#     time.sleep(random.randint(1, 3))
#     return n**2
#
#
# if __name__ == '__main__':
#
#     executor = ProcessPoolExecutor(max_workers=3)
#
#     futures = []
#     for i in range(10):
#         future = executor.submit(task, i)
#         futures.append(future)
#
#     executor.shutdown(True)
#     print('++++>')
#     for future in futures:
#         print(future.result())


# 线程池
# from concurrent.futures import ThreadPoolExecutor
#
# import os, time, random
#
# def task(n):
#     print('%s is runing' % os.getpid())
#     time.sleep(random.randint(1, 3))
#     return n**2
#
#
# if __name__ == '__main__':
#
#     executor = ThreadPoolExecutor(max_workers=3)
#
#     futures = []
#     for i in range(10):
#         future = executor.submit(task, i)
#         futures.append(future)
#
#     executor.shutdown(True)
#     print('++++>')
#     for future in futures:
#         print(future.result())

# map 方法
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
# import os, time, random
#
#
# def task(n):
#     print('%s is runing' % os.getpid())
#     time.sleep(random.randint(1, 3))
#     return n**2
#
#
# if __name__ == '__main__':
#
#     executor = ThreadPoolExecutor(max_workers=3)
#
#     # for i in range(10):
#     #     future = executor.submit(task, i)
#
#     executor.map(task, range(1, 12))    # map取代了for+submit

# 回调函数

from concurrent.futures import ProcessPoolExecutor
import requests
import os


def get_page(url):
    print('<进程%s> get %s' % (os.getpid(), url))
    respone = requests.get(url)
    if respone.status_code == 200:
        return {'url': url, 'text': respone.text}


def parse_page(res):
    res = res.result()
    print('<进程%s> parse %s' % (os.getpid(), res['url']))
    parse_res = 'url:<%s> size:[%s]\n' % (res['url'], len(res['text']))
    with open('db.txt', 'a') as f:
        f.write(parse_res)


if __name__ == '__main__':
    urls = [
        'https://www.baidu.com',
        'https://www.python.org',
        'https://www.openstack.org',
        'https://help.github.com/',
        'http://www.sina.com.cn/'

    ]

    p = ProcessPoolExecutor(3)
    for url in urls:
        p.submit(get_page, url).add_done_callback(parse_page)   # parse_page拿到的是一个future对象obj，需要用obj.result()拿到结果