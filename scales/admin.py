from django.contrib import admin 

from .models import ScalesBrands, ScalesServiceProviders, Scales, ScalesStatus
admin.site.register(ScalesBrands)
admin.site.register(ScalesServiceProviders)
admin.site.register(Scales)
admin.site.register(ScalesStatus)