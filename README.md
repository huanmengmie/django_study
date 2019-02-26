# 随手记
1. 使用django-admin startproject project_name 命令创建项目
2. 使用python manage.py startapp app_name 命令创建应用
3. 在项目的settings.py模块中注册应用
4. 使用python manage.py runserver 启动项目

## 模型类orm操作
1. 在project的settings模块中注册app
2. 定义继承了models.Model类的模型类
3. 执行 python manage.py makemigrations app_name 命令生成
4. 执行 python manage.py sqlmigrate polls 0001 展示建表语句
5. 执行 python manage.py migrate 建表

### 查询方法相关
1. 方法

|命令|作用|返回值|参数|
|---|---|---|---|
|get|返回一条数据|单个对象|查询条件|
|all|返回所有数据|QuerySet||
|filter|返回满足条件的数据|QuerySet|查询条件|
|exclude|返回不满足条件的数据|QuerySet|查询条件|
|order_by|对查询结果进行排序|QuerySet|排序字段（多个）|

2.函数
from django.db.models import F,Q,Sum,Count,Max,Min

-F对象： 用于类属性之间的比较
-Q对象： 用于条件之间的逻辑关系 |，&，～

aggregate：进行聚合操作，返回值是一个字典，
进行聚合的时候需要先导入聚合类
count：返回结果集中数据的数目，返回值是一个数字


## 后台管理

### 创建用户
> python manage.py createsuperuser

### 自动化测试
在app的tests模块中编写测试代码，执行命令
> python manage.py test polls


