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

## 后台管理

### 创建用户
> python manage.py createsuperuser
