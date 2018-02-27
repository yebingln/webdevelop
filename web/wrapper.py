from django.shortcuts import HttpResponse,render_to_response,redirect

def Filter(befor_func,after_func):
    def outer(main_func):
        def wrapperr(request,*args,**kwargs):
            befor_result=befor_func(request)
            if(befor_result!=None):
                return befor_result
            main_result=main_func(request)
            if(main_result!=None):
                return main_result
            after_result=after_func(request)
            if(after_result!=None):
                return after_result
        return wrapperr
    return outer

def befor_index(request):
    print('befor')
    # return HttpResponse('Befor_index')
def after_index(request):
    print('after')
    return HttpResponse('After_index')

@Filter(befor_index,after_index)
def index(request):
    print('index')
    return HttpResponse('Index')