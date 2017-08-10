from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Sub_Category(models.Model):
    sub_category_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.category.category_name + " - " + self.sub_category_name

class Product(models.Model):
    name = models.CharField(max_length=1000)
    brand = models.CharField(max_length=100)
    short_description = models.CharField(max_length=1000)
    photo_url = models.CharField(max_length=1000)
    deal_link = models.CharField(max_length=1000)
    long_description = models.CharField(max_length=5000)
    old_price = models.FloatField()
    price = models.FloatField()
    sub_category = models.ForeignKey(Sub_Category,on_delete=models.CASCADE, null=True)
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.brand+" - "+self.name