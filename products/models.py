from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField()
    description = models.TextField(default="this is cool")
    price = models.TextField()
    date = models.TextField()
