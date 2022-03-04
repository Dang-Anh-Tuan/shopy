from dataclasses import field
from rest_framework import serializers
from .models import Brand, Clothes

class ClothesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clothes
        fields = '__all__'
        depth = 1


class BrandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Brand
        fields = '__all__'