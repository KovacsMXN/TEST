#INCLUDE
from django.urls import path, include
#INCLUDE FORKLIFT APP VIEWS
from .views import forklift_index

from .views import inspection_sheet_language, inspection_sheet_form_es, inspection_sheet_form_en, forklift_view

from .views import forklift_service_providers, forklift_brands, forklift_status, forklift_imagen_upload, forklift_add

from .views import forklift_holders, forklift_holders_view

#URL PATTERNS
urlpatterns = [
    #URL PATTERN INDEX
    path('', forklift_index, name='forklift_index_view'),
    path('json/', include('forklift.json')),
    #URL PATTERN VIEW
    path('view/<int:id>/', forklift_view, name='forklift_view'),
    path('add/', forklift_add, name='forklift_add'),
    path('imagen/upload/<int:id>/', forklift_imagen_upload, name='forklift_imagen_upload'),

#ServiceProviders
    path('service/providers/', forklift_service_providers, name='forklift_service_providers'),

#Holders
    path('holders/', forklift_holders, name='forklift_holders'),
    path('holders/view/<int:id>', forklift_holders_view, name='forklift_holders_view'),

#Brands
    path('brands/', forklift_brands, name='forklift_brands'),

#Status
    path('status/', forklift_status, name='forklift_status'),


    #URL PATTERN INSPECTION SHEET
    path('inspection/', inspection_sheet_language, name='inspection_sheet_language'),
    #URL PATTERN INSPECTION SHEET
    path('inspection/es/', inspection_sheet_form_es, name='inspection_sheet_form_es'),
    #URL PATTERN INSPECTION SHEET
    path('inspection/en/', inspection_sheet_form_en, name='inspection_sheet_form_en'),
]