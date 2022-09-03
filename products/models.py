from distutils.archive_util import make_zipfile
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=999)
    brand = models.CharField(max_length=999)
    retail_price = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length=9999)
    image = models.URLField(blank=True)

    def __str__(self):
        return self.name
