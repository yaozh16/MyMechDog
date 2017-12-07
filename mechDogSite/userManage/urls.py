from django.conf.urls import url

from . import views,command

app_name='userManage'

urlpatterns = [
    url(r'^$',views.main,name='user'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^command$',command.operate,name='operate'),
]
