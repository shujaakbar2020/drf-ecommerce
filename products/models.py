from django.db import models
from django.contrib.postgres.fields import ArrayField


class Category(models.Model):
    name = models.CharField(max_length=1000)
    sub_categories = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=999)
    brand = models.CharField(max_length=999)
    retail_price = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length=9999)
    image = ArrayField(models.URLField(blank=True))
    categoy = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
