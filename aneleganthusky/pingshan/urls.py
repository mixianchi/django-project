from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pingshan-home'),
    path('login/', views.login, name='pingshan-login'),
]