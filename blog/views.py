from django.shortcuts import render,get_object_or_404, redirect
from .models import Blog
from django.utils import timezone


# Create your views here.
from .models import Blog
def home(request):
    blogs=Blog.objects #모델로부터 전달받은 객체:쿼리셋  #메소드
    return render(request,'home.html', {'blogs': blogs})

def detail(request,blog_id):
    blog_detail= get_object_or_404(Blog, pk=blog_id)
    return render(request,'detail.html',{'blog':blog_detail})
def new(request):
    return render (request, 'new.html')


def create(request):
    blog=Blog()
    blog.title=request.POST['title']
    blog.body=request.POST['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect ('/blog/'+str(blog.id))


def update(request, blog_id):
    blog_update=get_object_or_404(Blog, pk=blog_id)
    if request.method =="POST":
        blog_update.title=request.POST['title']
        blog_update.body=request.POST['body']
        blog_update.pub_date=timezone.datetime.now()
        blog_update.save()
        return redirect('detail',blog_id)
    else:
         return render(request, 'update.html', {'blog': blog_update})


def delete(request,blog_id):
    blog_delete=get_object_or_404(Blog, pk=blog_id)
    blog_delete.delete()
    return redirect('home')

#쿼리셋과 메소드의 형식
# 모델.쿼리셋(objects).메소드