import json
import os
from urllib import request
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.core.paginator import Paginator

from campay.sdk import Client

from backend.models import *
from gleichefoundation.settings import BASE_DIR

# Create your views here.

def index(request):
    news_blogs = NewsBlog.objects.filter(publish=1).order_by('-date_created')[:3]
    volunteers = Volunteer.objects.filter(publish=1).order_by('-date_created')[:10]
    testimonials = Testimonial.objects.filter(publish=1).order_by('-date_created')[:10]
    slides = Slide.objects.filter(publish=1).order_by('-date_created')[:10]
    sponsors = Sponsor.objects.filter(publish=1).order_by('-date_created')
    causes = Cause.objects.filter(publish=1).order_by('-date_created')

    data = {
        'news_blogs':news_blogs,
        'volunteers': volunteers,
        'testimonials': testimonials,
        'slides': slides,
        'sponsors': sponsors,
        'causes': causes,
    }

    return render(request, "frontend/index.html", data)

def donate(request):
    return render(request, "frontend/donate.html")

def about(request):
    return render(request, "frontend/about.html")

def news_blog(request):
    news_blog = NewsBlog.objects.filter(publish=1).order_by('-date_created')
    paginator = Paginator(news_blog, 3)
    page_number = request.GET.get('page')
    paged_news_objs = paginator.get_page(page_number)

    data = {
        'news_blogs':paged_news_objs
    }
    return render(request, "frontend/news.html", data)

def executives(request):
    executives = Executive.objects.filter(publish=1)
    paginator = Paginator(executives, 3)
    page_number = request.GET.get('page')
    paged_exeutive_objs = paginator.get_page(page_number)

    data = {
        'executives':paged_exeutive_objs
    }
    return render(request, "frontend/executives.html", data)

def read_news_blog(request, id):
    news_blog = NewsBlog.objects.get(id=id)
    data = {
        'news_blog':news_blog
    }
    return render(request, "frontend/read_new_blog.html", data)

def upcoming_events(request):
    return render(request, "frontend/upcoming_event.html")


def become_volunteer(request):
    return render(request, "frontend/become_volunteer.html")

def contact(request):
    return render(request, "frontend/contact.html")

def login(request):
    return render(request, "frontend/login.html")

def volunteers(request):
    volunteers = Volunteer.objects.filter(publish=1)
    paginator = Paginator(volunteers, 3)
    page_number = request.GET.get('page')
    paged_objs = paginator.get_page(page_number)

    data = {
        'volunteers':paged_objs
    }
    return render(request, "frontend/volunteers.html", data)

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
        data = {
            'name': received_json_data['fullname'],
            'subject': received_json_data['subject'],
        }
    
        msg_html = render_to_string('frontend/custom-email.html', data)

        email = EmailMessage(
            f"{received_json_data['fullname']} Contacted Gleiche Foundation",
            msg_html,
            settings.EMAIL_HOST_USER,
            ['richardafoudo07@gmail.com', 'mrarctech@gmail.com'],
            )
        email.fail_silently = True
        email.content_subtype = "html"
        email.send()
        return redirect('home')

    return HttpResponseBadRequest("Bad request")


def be_a_volunteer(request):

    if request.method == "POST":
        received_json_data=json.loads(request.body)

        data = {
            'fullname': received_json_data['fullname'],
            'email': received_json_data['email'],
            'phone': received_json_data['phone'],
            'address': received_json_data['address'],
            'about_gleiche': received_json_data['about_gleiche'],
            'interest_about_gleiche': received_json_data['interest_about_gleiche'],
            'help_gleiche': received_json_data['help_gleiche'],
            'impact_gleiche' : received_json_data['impact_gleiche'],
            'particular_skill': received_json_data['particular_skill'],
            'anything_else': received_json_data['anything_else'],
            'autobiography': received_json_data['autobiography'],
        }
    
        msg_html = render_to_string('frontend/be_a_volunteer_email.html', data)
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
            ['richardafoudo07@gmail.com', 'mrarctech@gmail.com'],
            )
        email.fail_silently = True
        email.content_subtype = "html"
        email.send()
        return redirect('home')

    return HttpResponseBadRequest("Bad request")
