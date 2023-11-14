#INCLUDE
from django.urls import path, include

#INCLUDE INVENTORY APP VIEWS
from .views import inv_index

#URL PATTERNS
urlpatterns = [
    #URL PATTERN INDEX
    path('', inv_index, name='view_inv_index'),
]