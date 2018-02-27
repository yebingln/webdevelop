from django.shortcuts import render_to_response
from django.shortcuts import render_to_response,redirect
from django.template.context_processors import csrf
from django.utils.safestring import mark_safe
from django.shortcuts import HttpResponse
from web.Public_Fun import common,HTML_helper
from . import forms
from . import models


def list(request,id,alex):
    print(id,alex)
    return HttpResponse('index')

#ass数据库里添加数据name变量，Userinfo数据库里添加username=bing数据
def Add(request,name):
    models.ass.objects.create(hostname=name)
    models.Userinfo.objects.create(username='bing')


    return HttpResponse('ok')

def addtype(request):
    models.UserTpye.objects.create(name='cat')
    models.UserTpye.objects.create(name='dog')
    models.UserTpye.objects.create(name='pig')
    return HttpResponse('OK')


#删除数据
def Delete(request,id):
    models.ass.objects.get(id=id).delete()
    return HttpResponse('OK')

#更改数据
def Update(request,id,hostname):
    obj=models.ass.objects.get(id=id)
    obj.hostname=hostname
    obj.save()

    models.ass.objects.filter(id__gt=id).update(hostname=hostname)
    return HttpResponse('OK')

def Update_2(request,id,hostname):
    models.ass.objects.filter(id__gt=id).update(hostname=hostname)
    return HttpResponse('OK')

#查询数据
def Query(request,hostname):
    objlist = models.ass.objects.filter(hostname__contains=hostname)
    for item in objlist:
        print(item.id)

    #一对多关系查询
    obj=models.Userinfo.objects.filter(user_type__id=1)
    print(obj)

    models.ass.objects.all()   #获取ass数据库里所有数据
    models.ass.objects.all()[0:2]   #获取ass数据库里前两个数据
    models.ass.objects.all().values('id','hostname')
    models.ass.objects.all().order_by('id')   #根据id升序排序查询所有数据
    models.ass.objects.all().order_by('-id')  #根据id降序排序查询所有数据
    models.ass.objects.filter(id__in=[2,3])
    models.ass.objects.filter(hostname__icontains=hostname)   #忽略大小写
    return HttpResponse('OK')

def asslist(request):
    ass_list = models.ass.objects.all()
    return render_to_response('asslist.html',{'data':ass_list,'user':'alex'})

def Login(request):
    if request.method =='POST':
        user = request.POST.get('username',None)  #获取提交来的用户名
        pwd = request.POST.get('password',None)
        print(user,pwd)
        result = models.Userinfo.objects.get(username=user,password=pwd)
        if result:
            request.session['is_login']={'user':user}
            return redirect('/web/index/')
        else:
            #return render_to_response('login.html',{'status':'用户名密码错误'},context=csrf(request))
            return render_to_response('login.html', {'status': '用户名密码错误'})

    else:
        #return render_to_response('login.html',context=csrf(request))
        return render_to_response('login.html')


def index(request):
    is_login=request.session.get('is_login')

    if not is_login:
        return redirect('/web/login/')
    else:
        return render_to_response('index.html',{'use':is_login['user']})

def logout(request):
    del request.session['is_login']
    return redirect('/web/login')

def Register(request):
    registerForm=forms.RegisterForm()

    if request.method=='POST':
        form=forms.RegisterForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print(data)
        else:
            temp=form.errors.as_data()
            print(temp['email'][0])
            print(temp['email'][0].messages[0])
    return render_to_response('register.html',{'form':registerForm})

#表单操作
def FormAct(request):
    ret={'data':None,'error':""}
    obj=forms.Alogin()
    ret['data']=obj
    if request.method == 'POST':
        checkform=forms.Alogin(request.POST)
        # checkresult=checkform.is_valid()
        # print(checkresult)
        if checkform.is_valid():
            username=request.POST.get('username')
            email=request.POST.get('email')
            ip=request.POST.get('ip')
            print(username,email,ip)
        else:
            #djangp.forms.utils.ErrorDict
            #errorobj=checkform.errors.as_data().values()
            errorobj=checkform.errors.as_text()
            ret['error']=errorobj
            print(errorobj)
            ret['data']=checkform

    return render_to_response('index.html',ret)


    """
      if request.method =='POST':
        user = request.POST.get('username',None)  #获取提交来的用户名
        pwd = request.POST.get('password',None)
        print(user,pwd)
        result = models.Userinfo.objects.filter(username=user,password=pwd)
        if result==1:
            return HttpResponse('登录成功')
        else:
            return render_to_response('login.html',{'status':'用户名密码错误'})


    else:
        return render_to_response('login.html')
    """

#分页功能方法  cookie方法
def page(request,page):
    per_item=common.try_int(request.COOKIES.get('page_num',10),10)   #获取cookie
    print(per_item)
    count = models.hostip.objects.all().count()
    page= common.try_int(page, 1)
    pageobj=HTML_helper.Pageinfo(page,count,per_item)
    result=models.hostip.objects.all()[pageobj.start():pageobj.end()]
    page_string=HTML_helper.pager(page,pageobj.all_page_count())
    ret={'data':result,'count':count,'page':page_string,'per_itm':per_item}
    response=render_to_response('page.html',ret)
    #response.set_cookie('page_num',per_item)   #设置cookie
    return response

