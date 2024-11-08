# filters.py

import django_filters
from .models import Course

class CourseFilter(django_filters.FilterSet):
    # Define filters for fields you want to filter by
    age_category = django_filters.ChoiceFilter(choices=Course.age_choices)
    product_model = django_filters.ChoiceFilter(choices=Course.product_choice)
    level = django_filters.ChoiceFilter(choices=Course.level_choices)
    created_at = django_filters.DateTimeFromToRangeFilter()
    updated_at = django_filters.DateTimeFromToRangeFilter()
    
    class Meta:
        model = Course
        fields = ['age_category', 'product_model', 'level', 'created_at', 'updated_at']