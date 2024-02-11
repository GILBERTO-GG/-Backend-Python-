from django.db import models

# Create your models here.
class ProductModel(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    seller = models.CharField(max_length=100)  
    color = models.CharField(max_length=50)  
    product_dimensions = models.CharField(max_length=100)






