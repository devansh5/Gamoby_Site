from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.


from .models import *

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    pass

@admin.register(Design)
class DesignAdmin(ImportExportModelAdmin):
    pass

@admin.register(Color)
class ColorAdmin(ImportExportModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    pass

@admin.register(Size)
class SizeAdmin(ImportExportModelAdmin):
    pass

@admin.register(Happy)
class HappyAdmin(ImportExportModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(Contac)
class ContacAdmin(ImportExportModelAdmin):
    pass

@admin.register(Banner)
class BannerAdmin(ImportExportModelAdmin):
    pass

@admin.register(Notify)
class NotifyAdmin(ImportExportModelAdmin):
    pass

 