from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pingshan-home'),
    path('about/', views.about, name='pingshan-about'),
]