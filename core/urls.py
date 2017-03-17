from django.conf.urls import url, include

from views import *



urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^/create$', create, name='create')

]