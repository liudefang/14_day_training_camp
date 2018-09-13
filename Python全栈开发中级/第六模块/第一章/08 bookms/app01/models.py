from django.db import models

# Create your models here.


class Book(models.Model):   # 必须要继承的
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publishData = models.DateField()    # 出版日期
    author = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)     # 一共5位，保留两位小数
    publish = models.CharField(max_length=32)

    def __str__(self):
        return self.title
