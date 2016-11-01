from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
]