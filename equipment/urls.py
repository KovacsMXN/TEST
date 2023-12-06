#INCLUDE
from django.urls import path, include

#INCLUDE LADDERS APP VIEWS
from .views import equipment_index, equipment_add
from .views import equipment_manufacturers, equipment_manufacturers_add, equipment_manufacturers_view, equipment_manufacturers_edit, equipment_manufacturers_delete, equipment_manufacturers_json

#URL PATTERNS
urlpatterns = [
    #URL PATTERN INDEX
    path('', equipment_index, name='equipment_index'),
    path('add/', equipment_add, name='equipment_add'),

    #URL PATTERN MANUFACTURERS
    path('manufacturers/', equipment_manufacturers, name='equipment_manufacturers'),
    path('manufacturers/add/', equipment_manufacturers_add, name='equipment_manufacturers_add'),
    path('manufacturers/view/<int:id>/', equipment_manufacturers_view, name='equipment_manufacturers_view'),
    path('manufacturers/edit/<int:id>/', equipment_manufacturers_edit, name='equipment_manufacturers_edit'),
    path('manufacturers/delete/<int:id>/', equipment_manufacturers_delete, name='equipment_manufacturers_delete'),
    path('manufacturers/pull/', equipment_manufacturers_json, name='equipment_manufacturers_json'),
]