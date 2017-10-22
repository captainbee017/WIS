from django.db import models


# Create your models here.

class ItemCategory(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    product_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(ItemCategory, null=True, blank=True)
    product_id = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
