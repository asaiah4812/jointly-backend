from django.urls import path
from . import views

urlpatterns = [
    path('', views.email_list),
    path('create/', views.email_create)
]