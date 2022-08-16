from django.contrib import admin
from .models import Compromise, Maintenance

# Register your models here.

class CompromiseAdmin(admin.ModelAdmin):
  list_display = ('year', 'estimated_computers', 'total_computers', 'get_department')

admin.site.register(Compromise, CompromiseAdmin)
admin.site.register(Maintenance)