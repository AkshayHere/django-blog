from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

# Create your views here.
def home(request: HttpRequest):
    print(request)
    return HttpResponse('<h1>Dude Home</h1>')

def aboutUs(request):
    return HttpResponse('<h3>About Dude</h3>')