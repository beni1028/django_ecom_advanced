# Django modules
from django.contrib import admin

# Django locals
from .models import Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category_name', 'slug']
	prepopulated_fields = {'slug': ('category_name','id')}