#INCLUDE
from django.urls import path, include

#INCLUDE SCALES APP VIEWS
#IMPORT MAIN INDEX
from .views import scales_index, scales_index_json, scales_view, scales_add, scales_edit, scales_delete
#IMPORT BRANDS
from .views import scale_brands, scales_brands_json, scales_brands_edit, scales_brands_view, scales_brands_add, scales_brands_delete
#IMPORT STATUS
from .views import scales_status, scales_status_view, scales_status_add, scales_status_edit, scales_status_delete
#IMPORT SERVICE PROVIDERS
from .views import scales_serviceprovider, scales_serviceprovider_view, scales_serviceprovider_add, scales_serviceprovider_edit, scales_serviceprovider_delete

#URL PATTERNS
urlpatterns = [
    #URL PATTERN INDEX
    path('', scales_index, name='scales_index_view'),
    path('json/pull/', scales_index_json, name='scales_index_view_json'),
    path('view/<int:id>/', scales_view, name='scales_view'),
    path('add/', scales_add, name='scales_add'),
    path('edit/<int:id>/', scales_edit, name='scales_edit'),
    path('delete/<int:id>/', scales_delete, name='scales_delete'),

    #URL PATTERN BRANDS
    path('brands/', scale_brands, name='scale_brands_view'),
    path('brands/json/pull/', scales_brands_json, name='scales_brands_json'),
    path('brands/view/<int:id>/', scales_brands_view, name='scales_brands_view'),
    path('brands/add/', scales_brands_add, name='scales_brands_add'),
    path('brands/edit/<int:id>/', scales_brands_edit, name='scales_brands_edit'),
    path('brands/delete/<int:id>/', scales_brands_delete, name='scales_brands_delete'),

    #URL PATTERN STATUS
    path('status/', scales_status, name='scales_status_index'),
    path('status/view/<int:id>/', scales_status_view, name='scales_status_view'),
    path('status/add/', scales_status_add, name='scales_status_add'),
    path('status/edit/<int:id>/', scales_status_edit, name='scales_status_edit'),
    path('status/delete/<int:id>/', scales_status_delete, name='scales_status_delete'),

    #URL PATTERN STATUS
    path('serviceproviders/', scales_serviceprovider, name='scales_serviceprovider_index'),
    path('serviceproviders/view/<int:id>/', scales_serviceprovider_view, name='scales_serviceprovider_view'),
    path('serviceproviders/add/', scales_serviceprovider_add, name='scales_serviceprovider_add'),
    path('serviceproviders/edit/<int:id>/', scales_serviceprovider_edit, name='scales_serviceprovider_edit'),
    path('serviceproviders/delete/<int:id>/', scales_serviceprovider_delete, name='scales_serviceprovider_delete_view'),
]