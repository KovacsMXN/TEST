from django.urls import path
from autenticacion.views import logout_view, login_view
from .views import index, configuracion_staff_index, configuracion_staff_delete , configuracion_staff_edit, configuracion_staff_password_edit

#IMPORT CONFIG STORAGE VIEWS
from .views import configuracion_storage_index, configuracion_storage_json_response, configuracion_storage_json_delete, configuracion_staff_json_response, configuracion_storage_edit, configuracion_storage_add, main_general_settings_index
from .views import equipment_locations_index, equipment_locations_delete, configuracion_locations_edit, configuracion_locations_add

from .views import equipment_brands, equipment_brands_json_response, equipment_brands_edit, equipment_brands_delete
from django.contrib import admin

urlpatterns = [
    path('', main_general_settings_index, name='configuracion_index'),

    path('storage/', configuracion_storage_index, name='configuracion_storage_index'),
    path('storage/add/', configuracion_storage_add, name='configuracion_storage_add'),
    path('storage/edit/<int:id>/', configuracion_storage_edit, name='configuracion_storage_edit'),
    path('storage/ajax/request/', configuracion_storage_json_response, name='configuracion_storage_json_response'),
    path('storage/ajax/delete/<int:id>/', configuracion_storage_json_delete, name='configuracion_storage_json_delete'),

    path('equipment/locations/', equipment_locations_index, name='equipment_locations_index'),
    path('equipment/locations/add/', configuracion_locations_add, name='configuracion_locations_add'),
    path('equipment/locations/delete/<int:id>/', equipment_locations_delete, name='equipment_locations_delete'),
    path('equipment/locations/edit/<int:id>/', configuracion_locations_edit, name='configuracion_locations_edit'),

    path('equipment/brands/', equipment_brands, name='equipment_brands'),
    path('equipment/brands/edit/<int:id>/', equipment_brands_edit, name='equipment_brands_edit'),
    path('equipment/brands/delete/<int:id>/', equipment_brands_delete, name='equipment_brands_delete'),
    path('equipment/ajax/request/', equipment_brands_json_response, name='equipment_brands_json_response'),

    path('staff/', configuracion_staff_index, name='configuracion_staff_usuarios'),
    path('staff/ajax/request/', configuracion_staff_json_response, name='configuracion_staff_json_response'),
    path('staff/delete/<int:id>/', configuracion_staff_delete, name='configuracion_staff_delete'),
    path('staff/edit/password/<int:id>/', configuracion_staff_password_edit, name='configuracion_staff_password_edit'),
    path('staff/edit/<int:id>/', configuracion_staff_edit, name='configuracion_staff_usuarios_edit'),
]