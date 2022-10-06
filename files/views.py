from django.shortcuts import render
from rest_framework import generics
from files.serializers import FileSerializer
from .models import Files
# Create your views here.


class FileAll(generics.ListCreateAPIView):
    queryset = Files.objects.all()
    serializer_class = FileSerializer
