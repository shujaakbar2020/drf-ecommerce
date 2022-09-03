from dataclasses import fields
from rest_framework import serializers

from products.models import Product


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth=1