from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/',views.index),
    url(r'^list/(?P<id>\d*)/(?P<alex>\d*)/$',views.list),
    url(r'^list/(?P<alex>\d*)/',views.list,{'id':222}),
    url(r'^Add/(?P<name>\w*)/',views.Add),
    url(r'^Delete/(?P<id>\d*)/',views.Delete),
    url(r'^Update/(?P<id>\d*)/(?P<host>\w*)/',views.Update),
    url(r'^Query/(?P<hostname>\w*)/',views.Query),
    url(r'^asslist/$',views.asslist),
    url(r'^login/$',views.Login),
    url(r'^register/$',views.Register),
    url(r'^addtype/$',views.addtype),
    url(r'^FormAct/$',views.FormAct),
    url(r'^logout/$',views.logout),

    #分页功能
    # url(r'^page/(?P<page>\w*)',views.page),
    url(r'^page/(\d*)',views.page),



]
