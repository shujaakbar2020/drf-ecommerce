from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from shopping_cart.serializers import ShoppingCartSerializer
from shopping_cart.models import ShoppingCart


class CartList(generics.ListCreateAPIView):
    # queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ShoppingCart.objects.filter(user=user)