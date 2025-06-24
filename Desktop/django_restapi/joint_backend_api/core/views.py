from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Email
from .serializers import EmailSerializer

# Create your views here.

@api_view(['GET'])
def email_list(request):
    emails = Email.objects.all()
    serializer = EmailSerializer(emails, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def email_create(request):
    data = request.data
    serializer = EmailSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


