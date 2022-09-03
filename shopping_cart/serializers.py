from dataclasses import fields
from rest_framework import serializers

from shopping_cart.models import ShoppingCart


class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = '__all__'
        depth = 1