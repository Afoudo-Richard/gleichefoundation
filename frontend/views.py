import json
from urllib import request
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail,EmailMessage
from django.conf import settings

from campay.sdk import Client

# Create your views here.


def index(request):
    return render(request, "frontend/index.html")
def donate(request):
    return render(request, "frontend/donate.html")
def about(request):
    return render(request, "frontend/about.html")

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
    
    msg_html = render_to_string('frontend/custom-email.html', {'name': request.POST.get("fullname"), 'subject': request.POST.get("subject")})
    # send_mail(
    #     subject='Hello from ArcTest on VIP consultanc cameroon',
    #     message='A stunning message',
    #     from_email=settings.EMAIL_HOST_USER,
    #     recipient_list=['richardafoudo07@gmail.com'],
    #     html_message=msg_html,
    #     )

    email = EmailMessage(
        "Gleiche Foundation",
        msg_html,
        settings.EMAIL_HOST_USER,
        ['richardafoudo07@gmail.com', 'marcellusfon002@gmail.com'],
        )
    email.fail_silently = True
    email.content_subtype = "html"
    email.send()
    return redirect('home')
