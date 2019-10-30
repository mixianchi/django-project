from django.shortcuts import render
from .models import Appeal

posts = [
    {
        'author':'xin',
        'title':'page 1',
        'content':'first content'
    },
    {
        'author': 'haha',
        'title': 'page 2',
        'content': 'second content'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'pingshan/home.html', context)

def login(request):
    return render(request, 'pingshan/login.html', {'title': 'Login'})
"""
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
"""

# Create your views here.
