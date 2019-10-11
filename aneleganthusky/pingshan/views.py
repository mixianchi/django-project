from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('<h1>Pingshan Home</h1>')

def about(request):
    return HttpResponse('<h1>Pingshan About</h1>')
"""
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
"""

# Create your views here.
