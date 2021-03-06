import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *

# Create your views here.


def index(request):
    return render(request, 'backend/dashboard.html')


def news_blog(request):
    news_blogs = NewsBlog.objects.all().order_by('-date_created')

    data = {
        'news_blogs': news_blogs
    }
    return render(request, 'backend/news_blog.html', data)


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


def update_news_blog(request, id):
    news_blog = NewsBlog.objects.get(id=id)
    form = NewsBlogForm(instance=news_blog)
    context = {
        'form': form
    }
    if request.method == "POST":
        print(request.POST)
        form = NewsBlogForm(request.POST, request.FILES, instance=news_blog)
        if form.is_valid():
            form.save()
            return redirect('system_news_blog')
    return render(request, 'backend/forms/news_blog_form.html', context)


def change_news_allow_comment_status(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body)
        news_blog = NewsBlog.objects.get(id=int(received_json_data['news_id']))
        if news_blog.allow_public_comments == 0:
            news_blog.allow_public_comments = 1
        else:
            news_blog.allow_public_comments = 0
        news_blog.save()
        return JsonResponse({'success': True})


def change_publish_status(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body)
        news_blog = NewsBlog.objects.get(id=int(received_json_data['news_id']))
        if news_blog.publish == 0:
            news_blog.publish = 1
        else:
            news_blog.publish = 0
        news_blog.save()
        return JsonResponse({'success': True})
