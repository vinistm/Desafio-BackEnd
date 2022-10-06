from rest_framework import serializers
from .models import CNAB

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CNAB
        fields = "__all__"
