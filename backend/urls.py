
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="dashboard"),
    path('news_blog/', views.news_blog, name="news_blog"),
    

]