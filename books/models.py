"""
    orm操作
    1、在project的settings模块中注册app
    2、定义继承了models.Model类的模型类
    3、执行 python manage.py makemigrations app_name 命令生成
    4、执行 python manage.py migrate


"""

from django.db import models


# Create your models here.

class BookInfo(models.Model):
    name = models.CharField(max_length=60)
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class HeroInfo(models.Model):
    name = models.CharField(max_length=60)
    gender = models.IntegerField(default=1)
    skill = models.CharField(max_length=60, null=True)
    book_id = models.ForeignKey(BookInfo, on_delete=models.CASCADE)  # 外键

    def __str__(self):
        return self.name

