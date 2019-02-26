from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice


# 多行显示
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3  # 默认需要添加3个对象


# 单行显示，更紧凑
class ChoiceInline2(admin.TabularInline):
    model = Choice
    extra = 3  # 默认需要添加3个对象


class QuestionAdmin(admin.ModelAdmin):
    # https://docs.djangoproject.com/zh-hans/2.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
    list_display = ['id', 'pub_date', 'question_text', 'was_published_recently']  # 列表中显示的属性

    list_filter = ['pub_date']  # 侧边栏添加过滤器

    search_fields = ['question_text']  # 添加搜索框

    fields = ['pub_date', 'question_text']  # 表单显示的属性顺序
    # fieldsets = [  # 将表格拆分为字段集，不能与fields同时使用
    #     (None, {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]

    # 利用question和choice的one_to_many关系
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

# admin.site.register(Choice)
