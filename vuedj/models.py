from django.db import models

# Create your models here.
class Product(models.Model):
    #title
    name = models.TextField(max_length=200)
    description = models.TextField(blank=True, null=True) #description
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.FileField(upload_to='vuedj/vue_inte/public/img', max_length=500)
    created_at = models.DateTimeField(auto_now_add=True) #created_at

    def __str__(self):
        #return the task title
        return self.name