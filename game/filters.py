from .models import Product
import django_filters

class ProductFilter(django_filters.FilterSet):
    category=django_filters.CharFilter(field_name='category',distinct="True")
    class Meta:
        model=Product
        fields=['category']
