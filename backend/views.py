import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *

from gleichefoundation.settings import BASE_DIR


# Create your views here.


def template(request):
    return render(request, 'backend/template.html')


def index(request):
    return render(request, 'backend/dashboard.html')

############################# News & Blog ###################################

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
        'title': "Add News&Blog"
    })
            
            form.save()
            return redirect('system_news_blog')
        
    else:
        form = NewsBlogForm()

    context = {
        'form': form,
        'title': "Add News&Blog"
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
        'title': "Update News&Blog image",
        'update': True,
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
        'title': "Update News&Blog"
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


############################# Executives ###################################

def executives(request):
    executives = Executive.objects.all()

    data = {
        'executives': executives
    }
    return render(request, 'backend/executives.html', data)


def add_executive(request):
    if request.method == 'POST':
        form = ExecutiveForm(request.POST, request.FILES)
        if form.is_valid():         
            form.save()
            return redirect('system_executives')
        
    else:
        form = ExecutiveForm()

    context = {
        'form': form,
        'title': "Add Executive"
    }
    
    return render(request, 'backend/forms/executive_form.html', context)

def update_executive(request, id):
    news_blog = Executive.objects.get(id=id)
    if request.method == 'POST':
        form = ExecutiveForm(request.POST,request.FILES, instance=news_blog)
        if form.is_valid():
            form.save()
            return redirect('system_executives')
        
    else:
        form = ExecutiveForm(instance=news_blog)
        
    context = {
        'update': True,
        'form': form,
        'title': "Update Executive"
    }
    return render(request, 'backend/forms/executive_form.html', context)

def update_executive_image(request, id):
    news_blog = Executive.objects.get(id=id)
    if request.method == 'POST':
        form = ExecutiveForm(request.POST,request.FILES, instance=news_blog)
        if form.is_valid():
            form.save()
            return redirect('system_executives')
        
    else:
        form = ExecutiveForm(instance=news_blog)
        
    context = {
        'update': True,
        'form': form,
        'title': "Update Executive Image"
    }
    return render(request, 'backend/forms/executive_image_form.html', context)

def delete_executive(request, id):
    executive = Executive.objects.get(id=id)
    if request.method == 'POST':
        executive.delete()
        return HttpResponseRedirect('/system/executives')

    else:
        return HttpResponseRedirect('/system/executives')

        



def change_executive_publish_status(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body)
        news_blog = Executive.objects.get(id=int(received_json_data['id']))
        if news_blog.publish == 0:
            news_blog.publish = 1
        else:
            news_blog.publish = 0
        news_blog.save()
        return JsonResponse({'success': True})


############################# Volunteers ###################################

def volunteers(request):
    volunteers = Volunteer.objects.all()

    data = {
        'volunteers': volunteers
    }
    return render(request, 'backend/volunteers.html', data)


def add_volunteer(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST, request.FILES)
        if form.is_valid():

            if request.POST.get('next') == "true":
                return render(request, 'backend/forms/volunteer_image_form.html', {
        'form': form,
        'title': "Add Volunteer Image"
    })
            
            form.save()
            return redirect('system_volunteers')
        
    else:
        form = VolunteerForm()

    context = {
        'form': form,
        'title': "Add Volunteer"
    }
    
    return render(request, 'backend/forms/volunteer_form.html', context)

def update_volunteer(request, id):
    volunteer = Volunteer.objects.get(id=id)
    if request.method == 'POST':
        form = VolunteerForm(request.POST,request.FILES, instance=volunteer)
        if form.is_valid():
            form.save()
            return redirect('system_volunteers')
        
    else:
        form = VolunteerForm(instance=volunteer)
        
    context = {
        'update': True,
        'form': form,
        'title': "Update Executive"
    }
    return render(request, 'backend/forms/executive_form.html', context)

def update_volunteer_image(request, id):
    volunteer = Volunteer.objects.get(id=id)
    if request.method == 'POST':
        form = VolunteerForm(request.POST,request.FILES, instance=volunteer)
        if form.is_valid():
            form.save()
            return redirect('system_volunteers')
        
    else:
        form = VolunteerForm(instance=volunteer)
        
    context = {
        'update': True,
        'form': form,
        'title': "Update Volunteer Image"
    }
    return render(request, 'backend/forms/volunteer_image_form.html', context)

def delete_volunteer(request, id):
    volunteer = Volunteer.objects.get(id=id)
    if request.method == 'POST':
        volunteer.delete()
        return HttpResponseRedirect('/system/volunteers')

    else:
        return HttpResponseRedirect('/system/volunteers')

        



def change_volunteer_publish_status(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body)
        volunteer = Volunteer.objects.get(id=int(received_json_data['id']))
        if volunteer.publish == 0:
            volunteer.publish = 1
        else:
            volunteer.publish = 0
        volunteer.save()
        return JsonResponse({'success': True})




############################# Testimonials ###################################


def testimonial(request):
    testimonials = Testimonial.objects.all().order_by('-date_created')

    data = {
        'testimonials': testimonials
    }
    return render(request, 'backend/testimonial.html', data)


def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('system_testimonials')
        
    else:
        form = TestimonialForm()

    context = {
        'form': form,
        'title': "Add Testinomial"
    }
    
    return render(request, 'backend/forms/testimonial_form.html', context)

def update_testimonial(request, id):
    testimonial = Testimonial.objects.get(id=id)
    if request.method == 'POST':
        form = TestimonialForm(request.POST,request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('system_testimonials')
        
    else:
        form = TestimonialForm(instance=testimonial)
        
    context = {
        'update': True,
        'form': form,
        'title': "Update Testinomial"
    }
    return render(request, 'backend/forms/testimonial_form.html', context)


def delete_testimonial(request, id):
    testimonial = Testimonial.objects.get(id=id)
    if request.method == 'POST':
        testimonial.delete()
        return HttpResponseRedirect('/system/testimonials')

    else:
        return HttpResponseRedirect('/system/testimonials')

def change_testimonial_publish_status(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body)
        testimonial = Testimonial.objects.get(id=int(received_json_data['id']))
        if testimonial.publish == 0:
            testimonial.publish = 1
        else:
            testimonial.publish = 0
        testimonial.save()
        return JsonResponse({'success': True})


############################# Slides ###################################


def slides(request):
    slides = Slide.objects.all().order_by('-date_created')

    data = {
        'slides': slides
    }
    return render(request, 'backend/slides.html', data)


def add_slide(request):
    if request.method == 'POST':
        form = SlideForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('system_slides')
        
    else:
        form = SlideForm()

    context = {
        'form': form,
        'title': "Add Slide"
    }
    
    return render(request, 'backend/forms/slide_form.html', context)

def update_slide(request, id):
    slide = Slide.objects.get(id=id)
    if request.method == 'POST':
        form = SlideForm(request.POST,request.FILES, instance=slide)
        if form.is_valid():
            form.save()
            return redirect('system_slides')
        
    else:
        form = SlideForm(instance=slide)
        
    context = {
        'update': True,
        'form': form,
        'title': "Update Slide"
    }
    return render(request, 'backend/forms/slide_form.html', context)

def delete_slide(request, id):
    slide = Slide.objects.get(id=id)
    if request.method == 'POST':
        slide.delete()
        return HttpResponseRedirect('/system/slides')

    else:
        return HttpResponseRedirect('/system/slides')

def change_slide_publish_status(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body)
        testimonial = Slide.objects.get(id=int(received_json_data['id']))
        if testimonial.publish == 0:
            testimonial.publish = 1
        else:
            testimonial.publish = 0
        testimonial.save()
        return JsonResponse({'success': True})

############################# Sponsors ###################################


def sponsors(request):
    sponsors = Sponsor.objects.all().order_by('-date_created')

    data = {
        'sponsors': sponsors
    }
    return render(request, 'backend/sponsors.html', data)


def add_sponsor(request):
    if request.method == 'POST':
        form = SponsorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('system_sponsors')
        
    else:
        form = SponsorForm()

    context = {
        'form': form,
        'title': "Add Sponsor"
    }
    
    return render(request, 'backend/forms/sponsor_form.html', context)

def update_sponsor(request, id):
    sponsor = Sponsor.objects.get(id=id)
    if request.method == 'POST':
        form = SponsorForm(request.POST,request.FILES, instance=sponsor)
        if form.is_valid():
            form.save()
            return redirect('system_sponsors')
        
    else:
        form = SponsorForm(instance=sponsor)
        
    context = {
        'update': True,
        'form': form,
        'title': "Update Sponsor"
    }
    return render(request, 'backend/forms/sponsor_form.html', context)

def delete_sponsor(request, id):
    sponsor = Sponsor.objects.get(id=id)
    if request.method == 'POST':
        sponsor.delete()
        return HttpResponseRedirect('/system/sponsors')

    else:
        return HttpResponseRedirect('/system/sponsors')

def change_sponsor_publish_status(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body)
        sponsor = Sponsor.objects.get(id=int(received_json_data['id']))
        if sponsor.publish == 0:
            sponsor.publish = 1
        else:
            sponsor.publish = 0
        sponsor.save()
        return JsonResponse({'success': True})

############################# Causes ###################################

def causes(request):
    causes = Cause.objects.all().order_by('-date_created')

    data = {
        'causes': causes
    }
    return render(request, 'backend/causes.html', data)


def add_cause(request):
    if request.method == 'POST':
        form = CauseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('system_causes')   
    else:
        form = CauseForm()

    context = {
        'form': form,
        'title': "Add Cause"
    }
    
    return render(request, 'backend/forms/cause_form.html', context)

def update_cause(request, id):
    cause = Cause.objects.get(id=id)
    if request.method == 'POST':
        form = CauseForm(request.POST,request.FILES, instance=cause)
        if form.is_valid():
            form.save()
            return redirect('system_causes')
    else:
        form = CauseForm(instance=cause)
        
    context = {
        'update': True,
        'form': form,
        'title': "Update Cause"
    }
    return render(request, 'backend/forms/cause_form.html', context)

def delete_cause(request, id):
    cause = Sponsor.objects.get(id=id)
    if request.method == 'POST':
        cause.delete()
        return HttpResponseRedirect('/system/causes')

    else:
        return HttpResponseRedirect('/system/causes')

def change_cause_publish_status(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body)
        cause = Cause.objects.get(id=int(received_json_data['id']))
        if cause.publish == 0:
            cause.publish = 1
        else:
            cause.publish = 0
        cause.save()
        return JsonResponse({'success': True})


############################# Upcoming Events ###################################

def upcoming_events(request):
    upcoming_events = UpcomingEvent.objects.all().order_by('-date_created')

    data = {
        'upcoming_events': upcoming_events
    }
    return render(request, 'backend/upcoming_events.html', data)


def add_upcoming_event(request):
    if request.method == 'POST':
        form = UpcomingEventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('system_upcoming_events')   
    else:
        form = UpcomingEventForm()

    context = {
        'form': form,
        'title': "Add Upcoming Event"
    }
    
    return render(request, 'backend/forms/upcoming_event_form.html', context)

def update_upcoming_event(request, id):
    upcoming_event = UpcomingEvent.objects.get(id=id)
    if request.method == 'POST':
        form = UpcomingEventForm(request.POST,request.FILES, instance=upcoming_event)
        if form.is_valid():
            form.save()
            return redirect('system_upcoming_events')
    else:
        form = UpcomingEventForm(instance=upcoming_event)
        
    context = {
        'update': True,
        'form': form,
        'title': "Update Upcoming Event"
    }
    return render(request, 'backend/forms/upcoming_event_form.html', context)

def delete_upcoming_event(request, id):
    upcoming_event = Sponsor.objects.get(id=id)
    if request.method == 'POST':
        upcoming_event.delete()
        return HttpResponseRedirect('/system/upcoming_events')
    else:
        return HttpResponseRedirect('/system/upcoming_events')

def change_upcoming_event_publish_status(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body)
        upcoming_event = UpcomingEvent.objects.get(id=int(received_json_data['id']))
        if upcoming_event.publish == 0:
            upcoming_event.publish = 1
        else:
            upcoming_event.publish = 0
        upcoming_event.save()
        return JsonResponse({'success': True})


############################# Settings ###################################

def settings(request):

    if request.method == "POST":
        print(request.POST.get('allow_bottom_quotes_scroll_banner'))
        settings_data = { 
            'allow_bottom_quotes_scroll_banner': False if request.POST.get('allow_bottom_quotes_scroll_banner') == None else True,
            "facebook_link": request.POST.get('facebook_link'),
            "instagram_link": request.POST.get('instagram_link'),
            "youtube_link": request.POST.get('youtube_link'),
            "twitter_link": request.POST.get('twitter_link'),
            "whatsapp_phone_number": request.POST.get('whatsapp_phone_number'),
            "gleiche_email": request.POST.get('gleiche_email'),
            "our_mission": request.POST.get('our_mission'),
            "short_about_us": request.POST.get('short_about_us'),
        }

        settings_file = open(f'{BASE_DIR}/web_settings.json', "w+")
        settings_data = json.dumps(settings_data)
        settings_file.write(settings_data)
        settings_file.close()

        return redirect('system_settings')

    else:
        settings_file = open(f'{BASE_DIR}/web_settings.json', "r")
        settings_data = json.load(settings_file)

        data = {
            "title": "Settings",
        }
        settings_file.close()

        context = {**data, **settings_data}

        return render(request, 'backend/settings.html', context)