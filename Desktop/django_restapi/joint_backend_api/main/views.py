from django.shortcuts import render
from core.models import Email

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def email_list(request):
    emails = Email.objects.all().order_by('-created_at')
    return render(request, 'core/email_list.html', {'emails': emails})