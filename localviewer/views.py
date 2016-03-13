# -*- coding:utf-8 -*-
from django.http import HttpResponse
import os
import json

# Create your views here.

# 目录列表
def dirlist(request):
    # 读取列表并返回json
    childDirs = os.listdir('./static/images/')
    jsonStr = json.dumps(childDirs)
    # 返回简单响应
    return HttpResponse(jsonStr)

# 详情界面
def filelist(request, dir_id):
    # 读取列表
    childDirs = os.listdir('./static/images/')
    childDirSize = len(childDirs)
    # 读取目录名
    dir_id_int = int(dir_id)
    if(dir_id_int < childDirSize):
        dirName = childDirs[dir_id_int]
        files = os.listdir('./static/images/%s' % dirName)
        return HttpResponse(json.dumps(files))
    return HttpResponse("[]")
