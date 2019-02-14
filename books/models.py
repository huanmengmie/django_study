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
    age = models.IntegerField()
    pub_date = models.TimeField()
    price = models.IntegerField()
