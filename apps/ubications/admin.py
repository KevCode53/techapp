from django.contrib import admin
from .models import Ubication

# Register your models here.

class UbicationAdmin(admin.ModelAdmin):
  list_display = ('name', 'address', 'phone', 'department', 'estimated_computers', 'state')
  search_fields = ('name', 'address', 'phone', 'department__name')
  list_filter = ('department',)
  ordering = ('name',)
  autocomplete_fields = ('department',)

admin.site.register(Ubication, UbicationAdmin)