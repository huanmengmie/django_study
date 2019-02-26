from django.db import models
import datetime

# Create your models here.
from django.utils import timezone
from django.utils.timezone import now


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(days=1) < self.pub_date < now()

    was_published_recently.admin_order_field = 'pub_date'  # 排序字段
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'  # 更改表头


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
