from django.conf.urls import url

from . import views
app_name='visitorManage'
urlpatterns = [
    url(r'^$',views.main,name='visitor'),
]
