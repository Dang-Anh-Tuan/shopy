from statistics import mode
from django.db import models

# Create your models here.
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        db_table = 'brand'


class Clothes(models.Model):
    id = models.AutoField(primary_key=True)
    color = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'clothes'