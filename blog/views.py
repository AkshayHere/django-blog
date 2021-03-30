from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

posts = [
    {
        'author' : 'The Dude',
        'title' : 'Post One',
        'content' : 'I am the dude man.',
        'date_posted' : 'August 27. 2021',
    },
    {
        'author' : 'Walter Sobchek',
        'title' : 'Post Two',
        'content' : 'Mark it Zero !!!',
        'date_posted' : 'August 27. 2021',
    },
]

# Create your views here.
def home(request: HttpRequest):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def aboutUs(request):
    return HttpResponse('<h3>About Dude</h3>')