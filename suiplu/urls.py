from django.conf import settings
from django.conf.urls.static import static

#IMPORT DJANGO FUNCTIONS
from django.urls import path, include
from django.contrib import admin

#IMPORT LOGIN AND LOGOUT VIEW
from autenticacion.views import logout_view, login_view

#IMPORT INDEX VIEWS
from .views import index

#IMPORT EQUIPMENT VIEWS
from .views import equipment_index, equipment_view, equipment_request_json, equipment_imagen_delete_view, equipment_imagen_upload_view

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #URLS FOR LOGIN AND LOGOUT
    path('logout/', logout_view, name='logout_view'),
    path('login/', login_view, name='login_view'),

    #URL FOR DJANGO ADMIN
    path('administracion/', admin.site.urls),

    #URL FOR CONFIGURACION APP
    path('configuracion/', include('configuracion.urls')),

    #URL FOR EQUIPMENT APP
    path('equipment/', equipment_index, name='equipment_index'),
    #URL VIEW EQUIPMENT
    path('equipment/view/<int:id>/', equipment_view, name='equipment_view'),
    #URL VIEW IMAGEN EDIT
    path('equipment/imagen/delete/<int:id>/', equipment_imagen_delete_view, name='equipment_imagen_delete_view'),
    #URL VIEW IMAGEN UPLOAD
    path('equipment/imagen/upload/<int:id>/', equipment_imagen_upload_view, name='equipment_imagen_upload_view'),

    #URLS TO HANDLE EQUIPMENT APP REQUEST
    path('equipment/json/request/', equipment_request_json, name='equipment_request_json'),
    path('', index, name='index'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)