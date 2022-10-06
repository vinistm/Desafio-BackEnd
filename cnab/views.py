from cnab.serializers import FileSerializer
from .models import COMPANY
from rest_framework import generics


class FileView(generics.ListCreateAPIView):
    queryset = COMPANY.objects.all()
    serializer_class = FileSerializer