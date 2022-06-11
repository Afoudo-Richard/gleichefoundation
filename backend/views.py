from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request,'backend/dashboard.html')

def news_blog(request):
    news_blogs = NewsBlog.objects.all()

    data = {
        'news_blogs': news_blogs
    }
    return render(request,'backend/news_blog.html', data)

def add_news_blog(request):
    return render(request, 'backend/forms/news_blog_form.html')