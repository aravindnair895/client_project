from django.db import models

# Create your models here.

class TableStock(models.Model):
    item = models.CharField(max_length=100, null=True)
    stock = models.FloatField(null=True)
    unit = models.CharField(max_length=100, null=True)
    low_stock = models.IntegerField(null=True)
    notes = models.TextField(null=True)