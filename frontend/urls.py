
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('contact_gleiche/', views.contact_gleiche, name="contact_gleiche"),
    path('donate/', views.donate, name="donate"),
    path('donate/mobile_money/', views.donate_through_mobile_money, name="mobile_money"),
    path('about/', views.about, name="about"),

]