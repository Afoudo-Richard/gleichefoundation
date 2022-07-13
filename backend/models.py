
from django.db import models

# Create your models here.

class NewsBlog(models.Model):
    title = models.CharField(max_length=200, null=False)
    content = models.TextField()
    image = models.ImageField(upload_to="NewBlogThumbnail",null=True)
    publish = models.BooleanField(default=False)
    allow_public_comments = models.BooleanField(default=False)
    user_comment = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'news_blog'
        verbose_name_plural = 'news_blogs'

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
    info = models.TextField()

    def __str__(self) -> str:
        return self.fullname

class Comment(models.Model):
    fullname = models.CharField(max_length=200, null=False)
    email = models.EmailField()
    comment = models.TextField()
    news_blog = models.ForeignKey(NewsBlog, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.fullname