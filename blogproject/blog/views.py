from django.shortcuts import render ,redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm
# Create your views here.

def first(request):
    return render(request,'first.html')
def home(request):
    blogs = Blog.objects #클래스 안에 있는 object를 변수에 넣는다. => querySet이라고 한다.
    return render(request,'home.html',{'blogs':blogs})

def detail(request, blog_id):#read
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html',{'details': details})
def about_me(request):
    return render(request, 'about_me.html')
def email(request):
    return render(request, 'email.html')

def github(request):
    return render(request, 'github.html')
def instagram(request):
    return render(request, 'instagram.html')

def new(request):
    form = BlogForm(request.POST)
    return render(request, 'new.html',{'form':form})    
    

def create(request):
    form = BlogForm(request.POST,request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)#임시저장
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('/blog/' + str(new_blog.id))
    return redirect('home')

def edit(request,id):
    edit_blog = Blog.objects.get(id=id)
    return render(request,'edit.html',{'blogs':edit_blog})

def update(request,id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.image = request.FILES['image']
    update_blog.save()
    return redirect('/blog/' + str(update_blog.id))

def delete(request,id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')
