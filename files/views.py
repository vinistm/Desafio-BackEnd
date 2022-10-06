from django.shortcuts import render
from rest_framework import generics
from files.serializers import FileSerializer
from .models import CNAB
# Create your views here.


class ViewFile(generics.ListCreateAPIView):
    queryset = CNAB.objects.all()
    serializer_class = FileSerializer
