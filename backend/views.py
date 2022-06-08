from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'backend/dashboard.html')
def news_blog(request):
    return render(request,'backend/news_blog.html')