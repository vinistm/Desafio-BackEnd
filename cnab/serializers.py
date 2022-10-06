from rest_framework import serializers
from .models import COMPANY

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = COMPANY
        fields = "__all__"