from django.db import models

# Create your models here.

class UserType(models.Model):
    """
    用户类型表,个数经常变动
    """
    title = models.CharField(max_length=32)


class UserInfo(models.Model):
    """
    用户表：讲师和班主任
    """
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=32)
    ut = models.ForeignKey(to="UserType", on_delete=models.CASCADE)
