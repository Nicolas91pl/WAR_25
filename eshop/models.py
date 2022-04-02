from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    added = models.DateTimeField(auto_now_add=True)
