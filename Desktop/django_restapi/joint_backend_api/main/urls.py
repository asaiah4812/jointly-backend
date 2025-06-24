from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('emails/', views.email_list, name='email_list'),
]
