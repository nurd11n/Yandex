from django.contrib import admin
from .models import Category, Car


admin.site.register(Car)
admin.site.register(Category)