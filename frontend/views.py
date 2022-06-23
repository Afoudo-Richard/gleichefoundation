import json
import os
from urllib import request
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail,EmailMessage
from django.conf import settings

from campay.sdk import Client

from backend.models import *

# Create your views here.


def index(request):
    news_blog = NewsBlog.objects.filter(publish=1).order_by('-date_created')[:3]

    data = {
        'news_blogs':news_blog
    }

    return render(request, "frontend/index.html", data)

def donate(request):
    return render(request, "frontend/donate.html")

def about(request):
    return render(request, "frontend/about.html")

def news_blog(request):
    news_blog = NewsBlog.objects.filter(publish=1).order_by('-date_created')
    data = {
        'news_blogs':news_blog
    }
    return render(request, "frontend/news.html", data)

def read_news_blog(request, id):
    news_blog = NewsBlog.objects.get(id=id)
    data = {
        'news_blog':news_blog
    }
    return render(request, "frontend/read_new_blog.html", data)

def upcoming_events(request):
    return render(request, "frontend/upcoming_event.html")

def executives(request):
    return render(request, "frontend/executives.html")

def become_volunteer(request):
    return render(request, "frontend/become_volunteer.html")

def contact(request):
    return render(request, "frontend/contact.html")

def login(request):
    return render(request, "frontend/login.html")

def volunteers(request):
    return render(request, "frontend/volunteers.html")

def picture_gallery(request):
    return render(request, "frontend/picture_gallery.html")


def donate_through_mobile_money(request):

    if request.method == "POST":
        received_json_data=json.loads(request.body)
        print(received_json_data)
        campay = Client({
            "app_username" : "uT2nFJcX0_Q9JuJPU3fRzKi0KhAMo2105QYRD9n8LqpXXck27aST07Hsfzw7uhPjZCpVuG48lSBPOFsWbov7CQ",
            "app_password" : "jEbwhec6ygiJGwAArWF_VTK_pfmMv3C9N_GriRosTbOFZGd326y1bAiXEme9EmpJVVH9FPByPfkOAmnJ8oJOig",
        "environment" : "DEV" #use "DEV" for demo mode or "PROD" for live mode
        })

        collect = campay.collect({
         "amount": "100", #The amount you want to collect
         "currency": "XAF",
         "from": received_json_data['phone'], #Phone number to request amount from. Must include country code
         "description": "some description"
        })

        print(collect)
        print("Data was posted")
        
    return render(request, "frontend/mobile_money.html")

def contact_gleiche(request):

    if request.method == "POST":
        received_json_data=json.loads(request.body)
        print(received_json_data)
    
        msg_html = render_to_string('frontend/custom-email.html', {'name': request.POST.get("fullname"), 'subject': request.POST.get("subject")})
        # send_mail(
        #     subject='Hello from ArcTest on gleiche foundation,
        #     message='A stunning message',
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=['richardafoudo07@gmail.com'],
        #     html_message=msg_html,
        #     )

        email = EmailMessage(
            "Gleiche Foundation",
            msg_html,
            settings.EMAIL_HOST_USER,
            ['richardafoudo07@gmail.com'],
            )
        email.fail_silently = True
        email.content_subtype = "html"
        email.send()
        return redirect('home')

    return HttpResponseBadRequest("asdfas asd fasd")
