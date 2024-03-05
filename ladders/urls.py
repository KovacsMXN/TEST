#INCLUDE
from django.urls import path, include

#INCLUDE LADDERS APP VIEWS
#IMPORT MAIN INDEX
from .views import ladders_index, ladders_index_json, ladders_view, ladders_add, ladders_delete, ladders_edit
#IMPORT MATERIALS
from .views import ladders_materials, ladders_materials_json, ladders_materials_add, ladders_materials_view, ladders_materials_edit, ladders_materials_delete
#IMPORT STATUS
from .views import ladders_status, ladders_status_add, ladders_status_view, ladders_status_delete, ladders_status_edit
#IMPORT INSPECTION
from .views import ladders_inspection, ladders_inspection_add
#IMPORT BRANDS
from .views import ladders_brands, ladders_brands_json, ladders_brands_view, ladders_brands_edit, ladders_brands_add, ladders_brands_delete

urlpatterns = [
    #URL PATTERN INDEX
    path('', ladders_index, name='ladders_index_view'),
    path('view/<int:id>/', ladders_view, name='ladders_view'),
    path('edit/<int:id>/', ladders_edit, name='ladders_edit'),
    path('add/', ladders_add, name='ladders_add'),
    path('delete/<int:id>', ladders_delete, name='ladders_delete'),
    path('json/pull/', ladders_index_json, name='ladders_index_view_json'),

    #URL PATTERN BRANDS
    path('brands/', ladders_brands, name='ladders_brands'),
    path('brands/view/<int:id>/', ladders_brands_view, name='ladders_brands_view'),
    path('brands/edit/<int:id>/', ladders_brands_edit, name='ladders_brands_edit'),
    path('brands/add/', ladders_brands_add, name='ladders_brands_add'),
    path('brands/delete/<int:id>/', ladders_brands_delete, name='ladders_brands_delete'),
    path('json/pull/brands/', ladders_brands_json, name='ladders_brands_json'),

    #URL PATTERN MATERIALS
    path('materials/', ladders_materials, name='ladders_materials'),
    path('materials/add/', ladders_materials_add, name='ladders_materials_add'),
    path('materials/view/<int:id>/', ladders_materials_view, name='ladders_materials_view'),
    path('materials/edit/<int:id>/', ladders_materials_edit, name='ladders_materials_edit'),
    path('materials/delete/<int:id>/', ladders_materials_delete, name='ladders_materials_delete'),
    path('json/pull/materials/', ladders_materials_json, name='ladders_materials_json'),

    #URL PATTERN STATUS
    path('status/', ladders_status, name='ladders_status'),
    path('status/add/', ladders_status_add, name='ladders_status_add'),
    path('status/view/<int:id>/', ladders_status_view, name='ladders_status_view'),
    path('status/edit/<int:id>/', ladders_status_edit, name='ladders_status_edit'),
    path('status/delete/<int:id>/', ladders_status_delete, name='ladders_status_delete'),

    #URL PATTERN INSPECTION
    path('inspection/', ladders_inspection, name='ladders_inspection'),
    path('inspection/add/<int:id>/', ladders_inspection_add, name='ladders_inspection_add'),

]