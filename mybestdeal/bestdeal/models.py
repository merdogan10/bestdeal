from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from datetime import datetime

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class Sub_Category(models.Model):
    sub_category_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.category.category_name + " - " + self.sub_category_name

class Affiliate(models.Model):
    name = models.CharField(max_length=1000)
    website = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=1000)
    brand = models.CharField(max_length=100)
    short_description = models.CharField(max_length=5000)
    photo_url = models.CharField(max_length=1000)
    deal_link = models.CharField(max_length=1000)
    long_description = models.CharField(max_length=7000, null=True)
    old_price = models.FloatField()
    price = models.FloatField()
    sub_category = models.ForeignKey(Sub_Category,on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    slug = models.SlugField(('slug'), max_length=300, blank=True)
    affiliate = models.ForeignKey(Affiliate, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.brand+" - "+self.name

    def offdeal(self):
        return round(100*(self.old_price-self.price)/self.old_price)

class Ads(models.Model):
    amzn_assoc_asins = models.CharField(max_length=1000)
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.amzn_assoc_asins+" - "+self.sub_category.category.category_name+" - "+self.sub_category.sub_category_name