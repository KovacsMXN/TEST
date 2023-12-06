#IMPORT DJANGO FUNCTIONS
from django.urls import path
from django.contrib import admin

#IMPORT VIEWS FOR STAFF SECTTION
from .views import staff_index, staff_view, staff_add, staff_edit, staff_password_edit, staff_json_response, staff_json_delete

#URLS PATTERNS START HERE
urlpatterns = [

#URL SECTION FOR STAFF
    #INDEX
        path('', staff_index, name='staff_index'),

        path('view/<int:id>/', staff_view, name='staff_view'),

        path('add/', staff_add, name='staff_add'),

        path('edit/<int:id>/', staff_edit, name='staff_edit'),
    #JSON DB RESPONSE
        path('json/pull/', staff_json_response, name='staff_json_response'),
    #DELETE
        path('json/delete/<int:id>/', staff_json_delete, name='staff_json_delete'),
    #EDIT PASSWORD
        path('password/edit/<int:id>/', staff_password_edit, name='staff_password_edit'),
    #EDIT GENERAL
        path('edit/<int:id>/', staff_edit, name='staff_edit'),
]