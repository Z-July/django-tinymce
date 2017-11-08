# -*-coding:utf-8 -*-
from django.contrib import admin
import models
# Register your models here.
class TestTinymce_Admin(admin.ModelAdmin):

    class Media:
        js = [
            '/static/tinymce/js/jquery.min.js',   # 必须首先加载的jquery，手动添加文件
            '/static/tinymce/js/tinymce/tinymce.min.js',   # tinymce自带文件
            '/static/tinymce/js/tinymce/plugins/jquery.form.js',    # 手动添加文件
            '/static/tinymce/js/tinymce/textarea.js',   # 手动添加文件，用户初始化参数
        ]

admin.site.register(models.TestTinymce, TestTinymce_Admin)
