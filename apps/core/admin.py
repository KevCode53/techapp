from django.contrib import admin
from .models import Department

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
  list_display = ('name', 'code')
  search_fields = ('name', 'code')

admin.site.register(Department, DepartmentAdmin)