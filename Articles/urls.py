from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    # url(r'(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^create/$', views.create_article, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.update_article, name='edit'),    
]