from django.contrib import admin
from .models import Category
from .models import Sub_Category
from .models import Product
from .models import Ads

admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Product)
admin.site.register(Ads)