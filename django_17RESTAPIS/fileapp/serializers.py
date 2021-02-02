from rest_framework import serializers

from .models import File

class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False)
    class Meta:
        model=File
        fields = '__all__'