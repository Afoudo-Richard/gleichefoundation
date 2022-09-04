from django.urls import path
from . import views

urlpatterns = [
    path('news_blogs/', views.NewsBlogList.as_view()),
]