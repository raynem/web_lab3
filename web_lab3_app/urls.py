from django.conf.urls import url
from web_lab3_app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^page1/$', views.page1, name='page1'),
    url(r'^page2/$', views.page2, name='page2'),
    url(r'^page3/$', views.page3, name='page3'),
    url(r'^post', views.post),
    url(r'^delete', views.delete),

]