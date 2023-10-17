from django.urls import path, include
from autenticacion.views import logout_view, login_view
from .views import index

from django.contrib import admin

from .views import equipment_index, equipment_request_json

urlpatterns = [
    # ...
    path('logout/', logout_view, name='logout_view'),
    path('login/', login_view, name='login_view'),
    path('admin/', admin.site.urls),
    path('configuracion/', include('configuracion.urls')),
    path('equipment/', equipment_index, name='equipment_index'),
    path('equipment/json/request/', equipment_request_json, name='equipment_request_json'),
    path('', index, name='index'),
]