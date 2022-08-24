"""
Models for this project
"""
from django.db import models


class Order(models.Model):
    """
    A simple order model
    """
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    last_updated = models.DateTimeField(auto_now=True, null=False)
    name = models.CharField(max_length=128, null=True, blank=True)


class OrderedItem(models.Model):
    """
    Items in an order
    """
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    last_updated = models.DateTimeField(auto_now=True, null=False)
    name = models.CharField(max_length=128, null=True, blank=True)
    sku = models.CharField(max_length=128, null=True, blank=True)
    count = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
