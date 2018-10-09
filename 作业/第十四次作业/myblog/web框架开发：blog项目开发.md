## 一、项目需求
    1 基于ajax和用户认证组件实现登录验证(10分)
    2 基于ajax和form组件实现注册功能(10分)
    3 系统首页文章列表的渲染(5分)
    4 个人站点页面设计(15)
    5 文章详细页的继承(10)
    6 点赞与踩灭(10)
    7 评论功能(20)
    8 富文本编辑器的使用(10)
    9 防止xss攻击(10)
    
## 二、项目实现
    基于ajax和form组件实现注册功能
    步骤一：
        在视图函数里面定义注册函数
        def register(request):
        在模板里面新建注册的模板文件
        register.html
        配置注册的路由：
        url(r'^register/$', views.register),
        
    步骤二：
        在视图函数里面定义登录函数
        def login(request):
        在模板里面新建登录的模板文件
        login.html
        配置登录的路由：
        url(r'^login/$', views.login),
        
    步骤三：
        在视图函数里面定义首页函数
        def index(request):
        在模板里面新建首页的模板文件
        index.html
        配置系统首页的路由
        url(r'^index/$', views.index),
        re_path('^$', views.index),
        
    步骤四：
        在视图函数定义个人站点函数
        def home_site(request, username, **kwargs):
        会区分访问是站点页面还是站点下的跳转页面
        在模板里面新建个人站点的模板文件，引用base.html
        home_site.html
        配置个人站点的路由
        # 个人站点url
        re_path('^(?P<username>\w+)/$', views.home_site),  # home_site(reqeust,username="yuan")

        # 个人站点的跳转
        re_path('^(?P<username>\w+)/(?P<condition>tag|category|archive)/(?P<param>.*)/$', views.home_site),
    
    步骤五：
        在视图函数里面定义文章详情页面的函数
        def article_detail(request, username, article_id):
        在模板里面新建文章详情页面的模板文件
        article_detail.html
        配置文章详情页面的路由
        re_path('^(?P<username>\w+)/articles/(?P<article_id>\d+)$', views.article_detail),
    
    步骤六：
           点赞功能的视图
        def digg(request):
        点赞功能用ajax实现：
        $("#div_digg .action").click(function () {
        
        点赞的路由配置
         path("digg/", views.digg),
         
    步骤七：
        评论功能的视图函数：
        def comment(request):
        获取评论树：
        def get_comment_tree(request):
        并实现的功能：
            1. 保存评论
            2. 创建事务
            3. 发送邮件
        评论功能使用ajax实现：
         $(".comment_btn").click(function () 
        点赞的路由配置：
        # 评论
        url(r'^comment/$', views.comment),
        # 获取评论树相关数据
        path("get_comment_tree/", views.get_comment_tree),
        
    步骤八：
        后台添加文章，编辑文章，删除文章，富文本编辑器使用
        视图：
        @login_required
        def add_article(request):
        KindEditor.ready(function (K)
        模板文件：
        add_article.html
        backend.html
        base.html
        路由配置:
        re_path("cn_backend/$", views.cn_backend),
        re_path("cn_backend/add_article/$", views.add_article),
        re_path(r'article/(\d+)/(delete|edit)', views.edit_article),
        
    步骤九：
        后台添加文章时，防止xss攻击
        # 防止xss攻击，过滤script标签
        soup = BeautifulSoup(content, "html.parser")
        for tag in soup.find_all():

            print(tag.name)
            if tag.name == "script":
                tag.decompose()
                
## 三、数据库模型设计
    class UserInfo(AbstractUser):
    """
    用户信息
    """
    class Blog(models.Model):
    """
    博客信息表（站点表）
    """
    class Category(models.Model):
    """
    博主个人文章分类表
    """
    class Tag(models.Model):
    """
    文章标签表
    """
    class Article(models.Model):
    """
    文章信息表
    """
    class Article2Tag(models.Model):
    """
    文章和标签关联表
    """
    class ArticleUpDown(models.Model):
    """
    点赞表
    """
    class Comment(models.Model):
    """
    评论表
    """
    
## 四、用户名和密码
    用户名：test1
    密码：123456
        
        