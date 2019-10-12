from django.shortcuts import render

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

def about(request):
    return render(request, 'pingshan/about.html')
"""
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
"""

# Create your views here.
