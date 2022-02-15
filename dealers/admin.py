from django.contrib import admin

# Register your models here.
from . models import Dealers

class DealerAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email', 'deal_date')
  list_display_links = ('id', 'name')
  search_fields = ('name',)
  list_per_page = 25


admin.site.register(Dealers, DealerAdmin)