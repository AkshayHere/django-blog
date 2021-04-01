from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from .models import Post

# Create your views here.
def home(request: HttpRequest):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def aboutUs(request):
    return render(request, 'blog/about.html')