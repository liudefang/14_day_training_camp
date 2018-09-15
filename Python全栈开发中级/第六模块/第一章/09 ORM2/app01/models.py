from django.db import models

# Create your models here.


class Book(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    publishDate = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    # 与Publish建立一对多的关系,外键字段建立在多的一方
    publish = models.ForeignKey(to="Publish", to_field="id", on_delete=models.CASCADE)
    # 与Author建立多对多的关系，ManyTOManyField可以建在两个模型中的任意一个，自动创建第三张表
    authors = models.ManyToManyField(to='Author',)

    def __str__(self):
        return self.title

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    # 与AuthorDetail建立一对一的关系
    authorDetail = models.OneToOneField(to="AuthorDetail", on_delete=models.CASCADE)


class Publish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return self.name

class AuthorDetail(models.Model):
    id = models.AutoField(primary_key=True)
    birthday = models.DateField()
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=64)  # 建立的一对一的关系
