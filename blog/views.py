# dojo/view.py

from django.shortcuts import get_object_or_404, render, redirect,render_to_response
#페이지 네이션
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

###########
from .models import CrawlingData
###########

from el_pagination.decorators import page_template
from django.template import RequestContext


def crawling(request):
    crawling = CrawlingData.objects.all().order_by('id')
    paginator = Paginator(crawling, 5)
    page = request.GET.get('page')

    try:
            crawling = paginator.page(page)
    except PageNotAnInteger:
            crawling = paginator.page(1)
    except EmptyPage:
            crawling = paginator.page(paginator.num_pages)
    
    context ={ 
         'crawling':crawling,
    }
    return render(request,'blog/crawlingdata_list.html', context)

def crawling_ajax(request): #Ajax 로 호출하는 함수
        crawling = CrawlingData.objects.all().order_by('id')
        paginator = Paginator(crawling,5)
        page = request.GET.get('page')
    
        try:
            crawling = paginator.page(page)
        except PageNotAnInteger:
            crawling = paginator.page(1)
        except EmptyPage:
            crawling = paginator.page(paginator.num_pages) #FIXEME: 데이터가 없으면 맨 끝 페이지를 계속 호출, 그러니 데이터가 이제 없다는 alert 넣기

        context = {'crawling':crawling}
        return render(request, 'blog/crawlingdata_list_ajax.html', context) #Ajax 로 호출하는 템플릿은 _ajax로 표시.

