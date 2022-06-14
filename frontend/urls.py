
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('contact_gleiche/', views.contact_gleiche, name="contact_gleiche"),
    path('donate/', views.donate, name="donate"),
    path('donate/mobile_money/', views.donate_through_mobile_money, name="mobile_money"),
    path('about/', views.about, name="about"),
    path('news_blog/', views.news_blog, name="news_blog"),
    path('news_blog/read/<int:id>', views.read_news_blog, name="read_news_blog"),
    path('upcoming_events/', views.upcoming_events, name="upcoming_events"),
    path('executives/', views.executives, name="executives"),
    path('become_volunteer/', views.become_volunteer, name="become_volunteer"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login, name="login"),
    path('volunteers/', views.volunteers, name="volunteers"),
    path('picture_gallery/', views.picture_gallery, name="picture_gallery"),
]