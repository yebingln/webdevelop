#coding='utf-8'
from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class MiddleWare(MiddlewareMixin):
    def process_request(self,request):
        print(1,'process_request')
        # return HttpResponse('404')
    def process_view(self,request,callback,callback_args,callback_kwrgs):
        print(1,'process_view')
    def process_exception(self,request,exception):
        print(1,'process_exception')
    def process_response(self,request,response):
        print(1,'process_response')
        return response