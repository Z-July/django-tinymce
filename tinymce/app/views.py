# -*-coding:utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import time
from PIL import Image
from django.conf import settings
from django.http import HttpResponse
# Create your views here.

static_base = 'http://127.0.0.1:8000'
static_url = static_base + settings.MEDIA_URL  # 上传文件展示路径前缀

# 上传图片 POST
@csrf_exempt
def upload_img(request):
    file = request.FILES['file']
    data = {
        'error':True,
        'path':'',
    }
    if file:
        timenow = int(time.time()*1000)
        timenow = str(timenow)
        try:
            img = Image.open(file)
            img.save(settings.MEDIA_ROOT + "content/" + timenow + unicode(str(file)))
        except Exception,e:
            print e
            return HttpResponse(json.dumps(data), content_type="application/json")
        imgUrl = static_url + 'content/' + timenow + str(file)
        data['error'] = False
        data['path'] = imgUrl
    return HttpResponse(json.dumps(data), content_type="application/json")
