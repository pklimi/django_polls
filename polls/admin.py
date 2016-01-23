# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Choice, Question

# Register your models here.

# 可同时添加多个Choice，以完整形式显示
# class ChoiceInline(admin.StackedInline):
# 可同时添加多个Choice，以简单表格形式显示
class ChoiceInline(admin.TabularInline):
    model = Choice
    # 默认提供3个Choice空间
    extra = 3

# 问题
class QuestionAdmin(admin.ModelAdmin):
    # 以指定顺序显示Question
    # fields = ['pub_date', 'question_text']
    
    # 把表单分割成字段集
    fieldsets = [
        (None,              {'fields' : ['question_text']}),
        # ('Date infomation', {'fields' : ['pub_date']}),
        # 为这一个字段集添加样式
        ('Date infomation', {'fields' : ['pub_date'], 'classes' : ['collapse']}),  
    ]
    # 在Question中直接显示多个Choice以供添加
    inlines = [ChoiceInline]
    # 在列表界面显示的字段
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 显示过滤器
    list_filter = ['pub_date']
    # 显示搜索框
    search_fields = ['question_text']

# 后台可管理Question表
#admin.site.register(Question)
# 后台管理时以指定方式显示Question
admin.site.register(Question, QuestionAdmin)

# 后台可管理Choice表
admin.site.register(Choice)
