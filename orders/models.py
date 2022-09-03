from django.conf import settings
from decimal import Decimal
from django.db import models
from django.contrib.postgres.fields import ArrayField

from users.models import MyUser
from products.models import Product


class Order(models.Model):
    date = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    delivery_method = models.CharField(max_length=50, default='')
    payment_method = models.CharField(max_length=50, default='')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orders', on_delete=models.CASCADE)
