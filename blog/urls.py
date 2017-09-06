#blog/ url.py
from django.conf.urls import url
from . import views



urlpatterns=[
   
    url(r'^board/$',views.board, name='board'),
    url(r'^crawling/$',views.crawling, name='crawling'),
    url(r'^crawling/ajax$',views.crawling_ajax, name='crawling_ajax'),

    
    url(r'^(?P<id>\d+)/$', views.board_detail, name='board_detail'), #url revrse를 사용한다면 view 가 역으로 url을 계산 url이 변경되어도 쉽게 대처 가능!
            
    url(r'^new/$', views.board_new, name='board_new'),   
  

    ]