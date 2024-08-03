from django.db import models


# Create your models here.
class Product_Card(models.Model):
    name= models.CharField(max_length=100, blank=False)
    image= models.ImageField(upload_to= 'product_card', blank=True, null= True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Product_Cards"