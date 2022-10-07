
from datetime import datetime
from email.policy import default
from enum import unique
import re
from unittest.util import _MAX_LENGTH
from django.db import models
from autoslug import AutoSlugField
from gleichefoundation.settings import MAIN_DOMAIN, MEDIA_ROOT_FOLDER

# Create your models here.

news_upload_to_dir = "NewBlogThumbnail"
executives_upload_to_dir = "ExecutivesImages"
volunteer_upload_to_dir = "VolunteerUserImages"
testimonial_images_upload_to_dir = "TestimonialUserImages"
slide_images_upload_to_dir = "Slides"
sponsor_images_upload_to_dir = "Sponsors"
upcoming_upload_to_dir = "UpcomingEvents"
causes_images_upload_to_dir = "Causes"


class NewsBlog(models.Model):
    title = models.CharField(max_length=200, null=False)
    content = models.TextField()
    image = models.ImageField(upload_to=news_upload_to_dir, default="default_news_image.jpg",blank=True)
    publish = models.BooleanField(default=False)
    allow_public_comments = models.BooleanField(default=False,)
    user_comment = models.TextField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title', unique_with='date_created__month')
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'news_blog'
        verbose_name_plural = 'news_blogs'
        ordering = ('-date_created',)

    def absolute_url(self):
        return f'{MAIN_DOMAIN}/news_blog/read/{self.slug}'
    
    def news_image(self):
        return f'{MAIN_DOMAIN}/{MEDIA_ROOT_FOLDER}{self.image.url}'

class UpcomingEvent(models.Model):
    title = models.CharField(max_length=200, null=False)
    caption = models.TextField(max_length=200, null=False)
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to=upcoming_upload_to_dir, default="default_user_image.png",blank=True)
    publish = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)


    def isPast(self):
        if self.date_time.date > datetime.date:
            return True
        return False

    def __str__(self) -> str:
        return self.title

class Volunteer(models.Model):
    image = models.ImageField(upload_to=volunteer_upload_to_dir, default="default_user_image.png",blank=True)
    firstname = models.CharField(max_length=200, null=False)
    lastname = models.CharField(max_length=200, null=False)
    publish = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    # facebook_link = models.CharField(max_length=500,)
    # instagram_link = models.CharField(max_length=500,)
    # twitter_link = models.CharField(max_length=500,)

    def __str__(self) -> str:
        return self.firstname + " " + self.lastname

    def fullName(self):
        return f"{self.firstname} {self.lastname}"

class Executive(models.Model):
    image = models.ImageField(upload_to=executives_upload_to_dir, default="default_user_image.png",blank=True)
    firstname = models.CharField(max_length=200, null=False)
    lastname = models.CharField(max_length=200, null=False)
    position = models.CharField(max_length=200, null=False)
    publish = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    # facebook_link = models.CharField(max_length=200, null=True, blank=True)
    # instagram_link = models.CharField(max_length=200, null=True, blank=True)
    # twitter_link = models.CharField(max_length=200, null=True, blank=True)
    # whatsapp_number = models.CharField(max_length=200, null=True, blank=True)
    info = models.TextField()

    def __str__(self) -> str:
        return self.firstname + " " + self.lastname

    def fullName(self):
        return f"{self.firstname} {self.lastname}"



class Cause(models.Model):
    title = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to=causes_images_upload_to_dir, default="default_user_image.png",blank=True)
    description = models.TextField()
    amount_needed = models.FloatField()
    amount_raised = models.FloatField(blank=True, default=0.0)
    date_created = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=False)

    def percentage_complete(self):
        if self.amount_raised == 0:
            return
        
        return (self.amount_raised/self.amount_needed)*100

    def __str__(self) -> str:
        return self.title
class PaymentMethod(models.Model):
    name = models.CharField(max_length=200,null=False)

class Donation(models.Model):
    fullname = models.CharField(max_length=200, null=False)
    amount = models.FloatField()
    method = models.CharField(max_length=200, null=False)
    cause = models.ForeignKey(Cause, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.fullname

class Sponsor(models.Model):
    name = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to=sponsor_images_upload_to_dir, default="default_user_image.png",blank=True)
    publish = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name

class Testimonial(models.Model):
    fullname = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to=testimonial_images_upload_to_dir, default="default_user_image.png",blank=True)
    occupation = models.TextField(null=False)
    testimony = models.TextField(null=False)
    publish = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)



    def __str__(self) -> str:
        return self.fullname

class Slide(models.Model):
    image = models.ImageField(upload_to=slide_images_upload_to_dir, default="default_user_image.png",blank=True)
    title = models.CharField(max_length=200, null=False)
    subtitle = models.TextField(null=False)
    publish = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    fullname = models.CharField(max_length=200, null=False)
    email = models.EmailField()
    comment = models.TextField()
    news_blog = models.ForeignKey(NewsBlog, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.fullname
