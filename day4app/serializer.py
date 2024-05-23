# serializer.py

from rest_framework import serializers
from .models import YourModel,Result

class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourModel
        # fields = ['name', 'semester']
        fields = '__all__'

# class ResultSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Result
#         fields = '__all__'        

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['name', 'semester', 'results', 'total_result']