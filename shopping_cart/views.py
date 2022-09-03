from django.shortcuts import render
from rest_framework import generics

from shopping_cart.serializers import ShoppingCartSerializer
from shopping_cart.models import ShoppingCart


class CartList(generics.ListCreateAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer