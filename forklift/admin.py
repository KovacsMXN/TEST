from django.contrib import admin

from .models import ForkliftOwners, ForkliftServiceProviders, ForkliftBrands, ForkliftStatus, Forklifts, InitialLoto, Loto, WaterEntry

admin.site.register(ForkliftOwners)
admin.site.register(ForkliftServiceProviders)
admin.site.register(ForkliftBrands)
admin.site.register(ForkliftStatus)
admin.site.register(Forklifts)
admin.site.register(InitialLoto)
admin.site.register(Loto)
admin.site.register(WaterEntry)