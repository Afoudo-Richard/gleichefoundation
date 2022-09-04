
from email.policy import default
from enum import unique
import re
from django.db import models
from autoslug import AutoSlugField
from gleichefoundation.settings import MAIN_DOMAIN, MEDIA_ROOT_FOLDER

# Create your models here.

news_upload_to_dir = "NewBlogThumbnail"

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
        return f'{MAIN_DOMAIN}/{MEDIA_ROOT_FOLDER}{self.image.url}/'

class UpcomingEvent(models.Model):
    title = models.CharField(max_length=200, null=False)
    date_time = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=200,)
    publish = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

class Voluteer(models.Model):
    firstname = models.CharField(max_length=200, null=False)
    lastname = models.CharField(max_length=200, null=False)
    email = models.EmailField()
    image = models.CharField(max_length=300,)
    facebook_link = models.CharField(max_length=500,)
    instagram_link = models.CharField(max_length=500,)
    twitter_link = models.CharField(max_length=500,)

    def __str__(self) -> str:
        return self.firstname + " " + self.lastname

class Executive(models.Model):
    firstname = models.CharField(max_length=200, null=False)
    lastname = models.CharField(max_length=200, null=False)
    info = models.TextField()

    def __str__(self) -> str:
        return self.firstname + " " + self.lastname

class Donation(models.Model):
    fullname = models.CharField(max_length=200, null=False)
    amount = models.FloatField()
    method = models.CharField(max_length=200, null=False)

    def __str__(self) -> str:
        return self.fullname

class Cause(models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.TextField()
    amount_needed = models.FloatField()
    amount_raised = models.FloatField()

    def __str__(self) -> str:
        return self.title

class Sponsor(models.Model):
    name = models.CharField(max_length=200, null=False)
    image = models.CharField(max_length=200,)

    def __str__(self) -> str:
        return self.name

class Testimonial(models.Model):
    fullname = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to="Testimonials", default="default_user_image.png",blank=True)
    occupation = models.TextField(null=False)
    testimony = models.TextField(null=False)
    date_created = models.DateTimeField(auto_now_add=True)



    def __str__(self) -> str:
        return self.fullname

class Comment(models.Model):
    fullname = models.CharField(max_length=200, null=False)
    email = models.EmailField()
    comment = models.TextField()
    news_blog = models.ForeignKey(NewsBlog, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.fullname