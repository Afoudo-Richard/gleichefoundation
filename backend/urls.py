
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="dashboard"),
    path('news_blog/', views.news_blog, name="news_blog"),
    path('news_blog/add/', views.add_news_blog, name="add_news_blog"),

    

]