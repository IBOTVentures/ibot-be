# filters.py

# import django_filters
from .models import Course,Product
from django_filters import rest_framework as filters

class CourseFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='product__category__category_name', lookup_expr='iexact')
    rating = filters.NumberFilter(field_name='rating', lookup_expr='gte')

    class Meta:
        model = Course
        fields = ['category', 'rating']

class ProductFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='category__category_name', lookup_expr='iexact')

    class Meta:
        model = Product
        fields = ['category']
