
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('contact_gleiche/', views.contact_gleiche, name="contact_gleiche")

]