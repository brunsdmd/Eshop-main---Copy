from django.db import models
from store.models.product import Products
from store.models.category import Category
from store.models.orders import Order


class EnquiryCat(models.Model):
    EnqCatName = models.CharField(max_length=128,null=False)
    def __str__(self):
        return self.EnqCatName

class CustEnq(models.Model):
    #Charfield is equal to varchar
    Email = models.EmailField()
    EnqCatName = models.ForeignKey(EnquiryCat,on_delete = models.CASCADE)
    EnqComment = models.CharField(max_length=128,null=False)

    def __str__(self):
        return self.EnqComment