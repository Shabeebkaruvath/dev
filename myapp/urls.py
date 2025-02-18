from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    path('about', views.about, name='about'),
    path('feedback', views.feedback, name='feedback'),
    path('service', views.service, name='service'),
    path('verify', views.check, name='check'),
    path('news', views.news, name='news'),
    path('short', views.short, name='short'),
     
]