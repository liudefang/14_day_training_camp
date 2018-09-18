from django.db import models

# Create your models here.


class Book(models.Model):   # 必须要继承的
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publishData = models.DateField()    # 出版日期
    authorlist = models.ManyToManyField(to="Author")
    price = models.DecimalField(max_digits=5, decimal_places=2)     # 一共5位，保留两位小数
    # 不用命名为publish_id，因为django为我们自动就加上了_id
    publish = models.ForeignKey(to="Publish", to_field="id", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Publish(models.Model):
    # 不写id的时候数据库会自动增加
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    # 与AuthorDetail建立一对一的关系

    def __str__(self):
        return self.name
