#blog/ url.py
from django.conf.urls import url
from . import views


urlpatterns=[
   
    url(r'^crawling/$',views.crawling, name='crawling'),
    url(r'^crawling/ajax$',views.crawling_ajax, name='crawling_ajax'),
  

    ]