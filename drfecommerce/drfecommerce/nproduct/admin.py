from django.contrib import admin
from .models import Brand, Category, Nproduct

# Register your models here.

admin.site.register(Nproduct)
admin.site.register(Category)
admin.site.register(Brand)
