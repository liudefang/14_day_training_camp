# -*- encoding: utf-8 -*-
# @Time    : 18-10-12 上午9:04
# @Author  : mike.liu
# @File    : Pagination.py
import copy


class Pagination(object):
    """
    自定义分页
    """
    def __init__(self, current_page, total_count, base_url, params, per_page_count=10, max_pager_count=11):
        try:
            current_page = int(current_page)
        except Exception as e:
            current_page = 1
        if current_page <=0:
            current_page = 1

        self.current_page = current_page

        # 数据总数
        self.total_count = total_count


        # 每页显示10条数据
        max_page_num, div = divmod(total_count, per_page_count)
        if div:
            max_page_num += 1
        self.max_page_num = max_page_num


        # 页面默认显示11个页码(当前页在中间）
        self.max_pager_count = max_pager_count
        self.half_max_pager_count = int((max_pager_count - 1)/2)


        # url前缀
        self.base_url = base_url

        # request.GET
        params = copy.deepcopy(params)
        params._mutable = True

        # 包含当前列表页面所有的搜索条件
        # {source:[2,], status:[2], gender:[2],consultant:[1],page:[1]}
        # self.params[page] = 8
        # self.params.urlencode()
        # source=2&status=2&gender=2&consultant=1&page=8
        # href="/hosts/?source=2&status=2&gender=2&consultant=1&page=8"
        # href="%s?%s" %(self.base_url,self.params.urlencode())
        self.params = params


    @property
    def start(self):
        return (self.current_page - 1) * self.per_page_count

    @property
    def end(self):
        return self.current_page * self.per_page_count

    def page_html(self):
        # 如果总页数<=11
        if self.max_page_num <= self.max_pager_count:
            pager_start = 1
            pager_end = self.max_page_num
        # 如果总页数 > 11
        else:
            # 如果当前页 <= 5
            if self.current_page <= self.half_max_pager_count:
                pager_start = 1
                pager_end = self.max_pager_count

            else:
                # 当前 + 5 > 总页码
                if (self.current_page + self.half_max_pager_count) > self.max_page_num:
                    pager_end = self.max_page_num
                    pager_start = self.max_page_num - self.max_pager_count + 1      # 倒这数11个
                else:
                    pager_start = self.current_page - self.half_max_pager_count
                    pager_end = self.current_page + self.half_max_pager_count

        page_html_list = []

        self.params['page'] = 1
        first_page = '<li><a href="%s?%s">首页</a></li>' %(self.base_url, self.params.urlencode(),)
        page_html_list.append(first_page)


        # 上一页
        self.params["page"] = self.current_page - 1
        if self.params["page"] < 1:
            pervious_page = '<li class="disabled"'
