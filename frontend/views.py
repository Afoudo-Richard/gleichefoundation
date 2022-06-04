from urllib import request
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail,EmailMessage
from django.conf import settings

# Create your views here.


def index(request):
    return render(request, "frontend/index.html")

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
        ['richardafoudo07@gmail.com'],
        )
    email.fail_silently = True
    email.content_subtype = "html"
    email.send()
    return redirect('home')
