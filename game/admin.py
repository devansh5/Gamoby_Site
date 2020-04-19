from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(Product)

admin.site.register(Profile)

admin.site.register(Design)

admin.site.register(Color)

admin.site.register(Item)

admin.site.register(Size)
