import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *

# Create your views here.


def template(request):
    return render(request, 'backend/template.html')


def index(request):
    return render(request, 'backend/dashboard.html')


def news_blog(request):
    news_blogs = NewsBlog.objects.all().order_by('-date_created')

    data = {
        'news_blogs': news_blogs
    }
    return render(request, 'backend/news_blog.html', data)


def add_news_blog(request):
    if request.method == 'POST':
        form = NewsBlogForm(request.POST, request.FILES)
        if form.is_valid():

            if request.POST.get('next') == "true":
                return render(request, 'backend/forms/news_image_form.html', {
        'form': form,
    })
            
            form.save()
            return redirect('system_news_blog')
        
    else:
        form = NewsBlogForm()

    context = {
        'form': form,
    }
    
    return render(request, 'backend/forms/news_blog_form.html', context)


def update_news_image(request, id):
    news_blog = NewsBlog.objects.get(id=id)
    if request.method == 'POST':
        form = NewsBlogForm(request.POST,request.FILES, instance=news_blog)
        if form.is_valid():
            form.save()
            return redirect('system_news_blog')
        
    else:
        form = NewsBlogForm(instance=news_blog)
        
    context = {
        'form': form,
    }
    return render(request, 'backend/forms/news_image_form.html', context)


def update_news_blog(request, id):
    news_blog = NewsBlog.objects.get(id=id)
    if request.method == 'POST':
        form = NewsBlogForm(request.POST,request.FILES, instance=news_blog)
        if form.is_valid():
            form.save()
            return redirect('system_news_blog')
        
    else:
        form = NewsBlogForm(instance=news_blog)
        
    context = {
        'form': form,
    }
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


def testimonial(request):
    testimonials = Testimonial.objects.all().order_by('-date_created')

    data = {
        'testimonials': testimonials
    }
    return render(request, 'backend/testimonial.html', data)
