from django.db import models
from django import utils

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True,default="this is cool")
    price = models.DecimalField(decimal_places=2,max_digits=10)
    summary = models.TextField(blank=False,null=False,default="this is summary")
    feature = models.BooleanField(default=False)
    date = models.DateField(default=utils.timezone.now)

