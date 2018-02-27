#coding='utf-8'
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
import json

def ajax(request):
    if request.method=='POST':
        print(request.POST)
        data={'status':0,'msg':'请求成功','data':[11,22,33,44]}
        return HttpResponse(json.dumps(data))
    else:
        return render_to_response('appajax/ajax.html')



def rout(request):
    return HttpResponse('OK')