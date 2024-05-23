# serializer.py

from rest_framework import serializers
from .models import YourModel

class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourModel
        # fields = ['name', 'semester']
        fields = '__all__'
