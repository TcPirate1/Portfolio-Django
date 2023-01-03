from django.contrib import admin
from .models import Categories

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('Title','category','language_framework')

# Register your models here.
admin.site.register(Categories, CategoriesAdmin)