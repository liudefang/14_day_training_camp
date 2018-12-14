# -*- encoding: utf-8 -*-
# @Time    : 2018/11/15 9:19 AM
# @Author  : mike.liu
# @File    : permission.py


def initial_session(user, request):
    permission = user.roles.all().values('permission__url').distinct()

    print(permission)
    # 去重后的所有权限!!将权限存在session中

    permission_list = []
    for item in permission:
        permission_list.append(item['permission__url'])

    print(permission_list)

    request.session['permission_list'] = permission_list