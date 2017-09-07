# dojo/view.py

from django.shortcuts import get_object_or_404, render, redirect,render_to_response
#페이지 네이션
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib import messages
from django.http import Http404
from .forms import PostForm

###########
from .models import CrawlingData
from .models import Post
###########

from el_pagination.decorators import page_template
from django.template import RequestContext


def notice(request):
    qs =  CrawlingData.objects.all()
    return render(request, 'blog/notice.html', {'crawling': qs})



def board(request):
    qs =  Post.objects.all()
    q = request.GET.get('q','')
    if q:
        qs = qs.filter(title__icontains = q)
    return render(request, 'blog/board.html',{'board': qs, 'q':q})

def board_detail(request, id):

    board = get_object_or_404(Post,id=id)  #위에 4가지 코드를 1줄로!
    return render(request, 'blog/board_detail.html', {'board': board})

def board_new(request):
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()  
            messages.success(request, '새 포스팅을 저장했습니다.')
            return redirect(post)  # 이미 model 에 post.get_absolute_url 함수를 구현 -->post_detail 로 이동
    
    else:
        form = PostForm
    return render(request, 'blog/board_form.html', {'form': form})




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

