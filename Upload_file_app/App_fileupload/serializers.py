from rest_framework import serializers
from .models import file

class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= file
        fields=['title','uploadedfile']
