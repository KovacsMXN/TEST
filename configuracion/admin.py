from django.contrib import admin
from .models import Storage_Locations, Equipment_Locations, Equipment_brands, Equipment, SupluMX

admin.site.register(Storage_Locations)
admin.site.register(Equipment_Locations)
admin.site.register(Equipment_brands)
admin.site.register(Equipment)
admin.site.register(SupluMX)