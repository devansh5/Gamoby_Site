from django.contrib import admin

# Register your models here.


from .models import Product,Profile

admin.site.register(Product)

admin.site.register(Profile)