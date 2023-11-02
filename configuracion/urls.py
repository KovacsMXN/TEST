#IMPORT DJANGO FUNCTIONS
from django.urls import path
from django.contrib import admin

#IMPORT LOG-IN AND LOG-OUT VIEWS 
from autenticacion.views import logout_view, login_view

#IMPORT VIEWS FOR STORAGE LOCATIONS SECTION
from .views import configuracion_storage_index, configuracion_storage_add, configuracion_storage_edit, configuracion_storage_json_response, configuracion_storage_json_delete

#IMPORT VIEWS FOR EQUIPMENT LOCATIONS 
from .views import equipment_locations_index, configuracion_locations_add, equipment_locations_delete, configuracion_locations_edit, equipment_locations_json_response

#IMPORT VIEWS FOR EQUIPMENT BRANDS
from .views import equipment_brands, equipment_brands_edit, equipment_brands_delete, equipment_brands_json_response

#IMPORT VIEWS FOR STAFF SECTTION
from .views import configuracion_staff_index, configuracion_staff_json_response, configuracion_staff_delete, configuracion_staff_password_edit, configuracion_staff_edit

#IMPORT VIEWS FOR INDEX
from .views import main_general_settings_index

#URLS PATTERNS START HERE
urlpatterns = [
#URL SECTION FOR MAIN INDEX
        path('', main_general_settings_index, name='configuracion_index'),


#URL SECTION FOR STORAGE LOCATIONS
    #INDEX
        path('storage/', configuracion_storage_index, name='configuracion_storage_index'),
    #ADD
        path('storage/add/', configuracion_storage_add, name='configuracion_storage_add'),
    #EDIT
        path('storage/edit/<int:id>/', configuracion_storage_edit, name='configuracion_storage_edit'),
    #JSON DB RESPONSE
        path('storage/ajax/request/', configuracion_storage_json_response, name='configuracion_storage_json_response'),
    #JSON DB DELETE
        path('storage/ajax/delete/<int:id>/', configuracion_storage_json_delete, name='configuracion_storage_json_delete'),


#URL SECTION FOR EQUIPMENT LOCATIONS
    #INDEX
        path('equipment/locations/', equipment_locations_index, name='equipment_locations_index'),
    #ADD
        path('equipment/locations/add/', configuracion_locations_add, name='configuracion_locations_add'),
    #JSON DB DELETE
        path('equipment/locations/delete/<int:id>/', equipment_locations_delete, name='equipment_locations_delete'),
    #EDIT
        path('equipment/locations/edit/<int:id>/', configuracion_locations_edit, name='configuracion_locations_edit'),
    #JSON DB RESPONSE
        path('equipment/locations/ajax/request/', equipment_locations_json_response, name='equipment_locations_json_response'),


#URL SECTION FOR EQUIPMENT BRANDS
    #INDEX
        path('equipment/brands/', equipment_brands, name='equipment_brands'),
    #EDIT
        path('equipment/brands/edit/<int:id>/', equipment_brands_edit, name='equipment_brands_edit'),
    #DELETE
        path('equipment/brands/delete/<int:id>/', equipment_brands_delete, name='equipment_brands_delete'),
    #JSON DB RESPONSE
        path('equipment/ajax/request/', equipment_brands_json_response, name='equipment_brands_json_response'),


#URL SECTION FOR STAFF
    #INDEX
        path('staff/', configuracion_staff_index, name='configuracion_staff_usuarios'),
    #JSON DB RESPONSE
        path('staff/ajax/request/', configuracion_staff_json_response, name='configuracion_staff_json_response'),
    #DELETE
        path('staff/delete/<int:id>/', configuracion_staff_delete, name='configuracion_staff_delete'),
    #EDIT PASSWORD
        path('staff/edit/password/<int:id>/', configuracion_staff_password_edit, name='configuracion_staff_password_edit'),
    #EDIT GENERAL
        path('staff/edit/<int:id>/', configuracion_staff_edit, name='configuracion_staff_usuarios_edit'),
]