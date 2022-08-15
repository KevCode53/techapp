from django.contrib import admin
from .models import Department

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
  list_display = ('name', 'id')
  search_fields = ('name', 'id')

admin.site.register(Department, DepartmentAdmin)