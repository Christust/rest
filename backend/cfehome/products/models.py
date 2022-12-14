from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    price =  models.DecimalField(decimal_places=2, max_digits=15)

    def __str__(self):
        return self.title
    
    @property
    def sale_price(self):
        return "%2f" %(float(self.price) * 0.8)