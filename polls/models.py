# -*- coding:utf-8 -*-
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

# 定义问题模型
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('datepublished')
    
    # 是否是最近添加的
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    # 在列表界面排序依赖另一字段
    was_published_recently.admin_order_field = 'pub_date'
    # 显示为Boolean型
    was_published_recently.boolean = True
    # 在列表界面显示的描述
    was_published_recently.sort_description = 'Published recently ?'
    
    # 显示自定义内容
    def __str__(self):
        return self.question_text
    
# 定义问题选项
class Choice(models.Model):
    # 多个选项对应一个问题
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    # 显示自定义内容
    def __str__(self):
        return self.choice_text
