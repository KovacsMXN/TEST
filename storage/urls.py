from django.urls import path

from .views import storage_index, storage_view, storage_add, storage_edit, storage_delete
from .views import locations_index, locations_view, locations_add, locations_edit, locations_delete

urlpatterns = [
    path("", storage_index, name="storage_index"),
    path("view/<int:id>/", storage_view, name="storage_view"),
    path("edit/<int:id>/", storage_edit, name="storage_edit"),
    path("add/", storage_add, name="storage_add"),
    path('delete/<int:id>/', storage_delete, name='storage_delete'),

    path("locations/", locations_index, name="locations_index"),
    path("locations/view/<int:id>/", locations_view, name="locations_view"),
    path("locations/edit/<int:id>/", locations_edit, name="locations_edit"),
    path("locations/add/", locations_add, name="locations_add"),
    path('locations/delete/<int:id>/', locations_delete, name='locations_delete'),
]