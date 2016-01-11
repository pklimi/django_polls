# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.

# 定义问题模型
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('datepublished')
    
# 定义问题选项
class Choice(models.Model):
    # 多个选项对应一个问题
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
