import csv
import io
import json
from itertools import product
from logging import raiseExceptions
import pandas as pd
import codecs
from urllib import response
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework import generics

from products.serializers import FileUploadSerializer, ProductSerializer
from products.models import Product, Category


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# RetrieveUpdateDestroyAPIView
class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UploadfileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            # category_tree = (json.loads(row['product_category_tree'])[0]).split(">>")
            # c = Category.objects.filter(name=category_tree[-2])
            product = Product(
                name=row['product_name'],
                brand=row['brand'],
                retail_price=int(row['retail_price']),
                price=int(row['discounted_price']),
                description=row['description'],
                image=json.loads(row['image']),
            )
            product.save()
        
        return Response({"status": "Products data uploaded successfully."}, status=status.HTTP_201_CREATED)