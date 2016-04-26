from django.conf.urls import patterns, url
from postreply import views


urlpatterns = patterns('',
        url(r'^$', views.home, name='home'),
        url(r'^home/add/$', views.addpost, name="addpost"),
        url(r'^getdata/$', views.getdata, name="getdata"),
        url(r'^home/$', views.postform, name="homepage"),
        url(r'^reply/$', views.addreply, name="addreply"),
        



        )