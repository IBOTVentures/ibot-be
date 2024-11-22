# filters.py

# import django_filters
from .models import Course
from django_filters import rest_framework as filters

class CourseFilter(filters.FilterSet):
    age_category = filters.CharFilter(field_name='age_category', lookup_expr='iexact')
    level = filters.CharFilter(field_name="level", lookup_expr='icontains')
    rating = filters.NumberFilter(field_name="rating", lookup_expr='gte')

    class Meta:
        model = Course
        fields = ['age_category', 'level', 'rating']


