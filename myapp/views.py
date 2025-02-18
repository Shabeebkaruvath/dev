from django.shortcuts import render
from django.http import JsonResponse
import urllib3

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def feedback(request):
    return render(request, 'feedback.html')

def service(request):
    return render(request, 'service.html')

def check(request):
    return render(request, 'linkverify.html')

def news(request):
    return render(request, 'news.html')

def short(request):
    return render(request, 'short.html')




 
