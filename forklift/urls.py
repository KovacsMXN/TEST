#INCLUDE GENERIC
from django.urls import path, include

#IMPORT FORKLIFTS
from .views import forklift_index, forklift_view, forklift_edit, forklift_add

#IMPORT VIEWS PROVIDERS
from .views import forklift_service_providers, forklift_service_providers_view, forklift_service_providers_add, forklift_service_providers_edit

#IMPORT VIEWS HOLDERS
from .views import forklift_holders, forklift_holders_view, forklift_holders_edit, forklift_holders_add

#IMPORT VIEW BRANDS
from .views import forklift_brands, forklift_brands_view, forklift_brands_edit, forklift_brands_add

#IMPORT VIEWS STATUS
from .views import forklift_status, forklift_status_view, forklift_status_edit, forklift_status_add

#IMPORT VIEWS LOTO
from .views import forklift_loto, forklift_loto_view, forklift_loto_add, forklift_loto_delete

#IMPORT VIEWS LOTO LOG
from .views import forklift_loto_log, forklift_loto_log_view, forklift_loto_log_add

#IMPORT VIEWS INSPECTION SHEET
from .views import inspection_sheet_language, inspection_sheet_form_es, inspection_sheet_form_en, inspection, inspection_log, inspection_view, inspection_release

#IMPORT VIEWS WATER TRAYCING
from .views import water_track_add, water_track

urlpatterns = [

#URL EXTRA (JSON) PATTERNS
    path('json/', include('forklift.json')),

#URL INDEX (FORKLIFTS)
    path('', forklift_index, name='forklift_index_view'),
    path('view/<int:id>/', forklift_view, name='forklift_view'),
    path('edit/<int:id>/', forklift_edit, name='forklift_edit'),
    path('add/', forklift_add, name='forklift_add'),

#WATER TRAYCING
    path('water/', water_track, name='water_track'),
    path('water/add/<int:id>/', water_track_add, name='water_track_add'),

#SERVICEPROVIDERS
    path('service/providers/', forklift_service_providers, name='forklift_service_providers'),
    path('service/providers/view/<int:id>/', forklift_service_providers_view, name='forklift_service_providers_view'),
    path('service/providers/edit/<int:id>/', forklift_service_providers_edit, name='forklift_service_providers_edit'),
    path('service/providers/add/', forklift_service_providers_add, name='forklift_service_providers_add'),

#HOLDERS
    path('holders/', forklift_holders, name='forklift_holders'),
    path('holders/view/<int:id>/', forklift_holders_view, name='forklift_holders_view'),
    path('holders/edit/<int:id>/', forklift_holders_edit, name='forklift_holders_edit'),
    path('holders/add/', forklift_holders_add, name='forklift_holders_add'),

#BRANDS
    path('brands/', forklift_brands, name='forklift_brands'),
    path('brands/view/<int:id>/', forklift_brands_view, name='forklift_brands_view'),
    path('brands/edit/<int:id>/', forklift_brands_edit, name='forklift_brands_edit'),
    path('brands/add/', forklift_brands_add, name='forklift_brands_add'),

#STATUS
    path('status/', forklift_status, name='forklift_status'),
    path('status/view/<int:id>/', forklift_status_view, name='forklift_status_view'),
    path('status/edit/<int:id>/', forklift_status_edit, name='forklift_status_edit'),
    path('status/add/', forklift_status_add, name='forklift_status_add'),

#LOTO
    path('loto/', forklift_loto, name='forklift_loto'),
    path('loto/view/<int:id>/', forklift_loto_view, name='forklift_loto_view'),
    path('loto/add/<int:id>/', forklift_loto_add, name='forklift_loto_add'),
    path('loto/delete/<int:id>/', forklift_loto_delete, name='forklift_loto_delete'),
#LOTO LOG
    path('loto/log/', forklift_loto_log, name='forklift_loto_log'),
    path('loto/log/view/<int:id>/', forklift_loto_log_view, name='forklift_loto_log_view'),
    path('loto/log/add/<int:id>', forklift_loto_log_add, name='forklift_loto_log_add'),

#INSPECTION SHEET
    path('inspection/', inspection, name='inspection'),
    path('inspection/log/', inspection_log, name='inspection_log'),
    path('inspection/view/<int:id>/', inspection_view, name='inspection_view'),
    path('inspection/release/<int:id>/', inspection_release, name='inspection_release'),
    path('drivers/', inspection_sheet_language, name='inspection_sheet_language'),
    path('drivers/es/', inspection_sheet_form_es, name='inspection_sheet_form_es'),
    path('drivers/en/', inspection_sheet_form_en, name='inspection_sheet_form_en'),
]