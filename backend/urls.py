
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="dashboard"),
    path('news_blog/', views.news_blog, name="system_news_blog"),
    path('news_blog/add/', views.add_news_blog, name="add_news_blog"),
    path('news_blog/update/<str:id>', views.update_news_blog, name="update_news_blog"),
    path('change_news_blog_allow_comment_status/', views.change_news_allow_comment_status, name="change_news_blog_allow_comment_status"),
    path('change_publish_status/', views.change_publish_status, name="change_publish_status"),
    path('template/', views.template, name="template"),
    path('update_news_image/<str:id>', views.update_news_image, name="update_news_image"),
    path('testimonial/', views.testimonial, name="system_testimonial"),


]