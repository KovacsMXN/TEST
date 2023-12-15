#IMPORT GENERIC 
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

#IMPORT LOGIN AND LOGOUT VIEW
from autenticacion.views import logout_view, login_view

#IMPORT LOGIN AND LOGOUT VIEW
from autenticacion.views import ins_logout_view, ins_login_view

#IMPORT INDEX VIEWS
from .views import index

#IMPORT EQUIPMENT VIEWS
from .views import equipment_index, equipment_view, equipment_request_json, equipment_imagen_upload_view, equipment_delete

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

    #URLS FOR LOGIN AND LOGOUT ( FORKLIFT DRIVERS)
    path('drivers/logout/', ins_logout_view, name='ins_logout_view'),
    path('drivers/login/', ins_login_view, name='ins_login_view'),

    #URL FOR DJANGO ADMIN
    path('administracion/', admin.site.urls),

    #URL FOR CONFIGURACION APP
    path('equipment/', include('equipment.urls')),

    #URL FOR FORKLIFTS APP
    path('forklifts/', include('forklift.urls')),

    #URL FOR LADDERS APP
    path('ladders/', include('ladders.urls')),

    #URL FOR INVENTORY APP
    path('inventory/', include('inventory.urls')),

    #URL FOR STORAGE APP
    path('storage/', include('storage.urls')),

    #URL FOR STAFF APP
    path('staff/', include('staff.urls')),

    #URL FOR INDEX
    path('', index, name='index'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)