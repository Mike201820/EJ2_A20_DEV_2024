# stringapp/serializers.py
from rest_framework import serializers
from .models import StringCalculation

class StringCalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StringCalculation
        fields = '__all__'
