# -*-coding:utf-8 -*-
from django.db import models

# Create your models here.


class TestTinymce(models.Model):
    title = models.CharField("标题", max_length=20, default="")
    content = models.TextField("文本", default="")

    class Meta:
        db_table = "test_tinymce"
        verbose_name = "测试"
        verbose_name_plural = "测试"

    def __unicode__(self):
        return self.title