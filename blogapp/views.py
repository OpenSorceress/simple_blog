from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from blogapp.models import BlogArticle
# Create your views here.

def index(request):
    blogs = BlogArticle.objects.all()
    if request.method == 'POST':
        usrname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=usrname, password=pwd)
        if user is not None:
            login(request,user)
            return render(request, 'index.html', {'testvar': 'Test String2!', 'blogs': blogs, 'user': user})
    return render(request, 'index.html', {'testvar': 'Test String2!', 'blogs': None})

def createBlog(request, blogs, user):
    newBlog = BlogArticle()
    newBlog.title = request.POST('title')
    newBlog.author = request.user
    newBlog.blog_content = request.POST('blog_content')
    newBlog.save()
    return render(request, 'index.html', {'testvar': 'Test String2!', 'blogs': blogs, 'user': user})