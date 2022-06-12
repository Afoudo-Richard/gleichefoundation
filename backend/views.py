from django.shortcuts import redirect, render
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request,'backend/dashboard.html')

def news_blog(request):
    news_blogs = NewsBlog.objects.all().order_by('-date_created')

    data = {
        'news_blogs': news_blogs
    }
    return render(request,'backend/news_blog.html', data)

def add_news_blog(request):
    context = {}
    if request.method == "POST":
        print(request.POST)
        form = NewsBlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {
                'form': form
            }
            return redirect('system_news_blog')
        print(form.errors)
    return render(request, 'backend/forms/news_blog_form.html', context)