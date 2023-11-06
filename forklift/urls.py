#INCLUDE
from django.urls import path, include

#INCLUDE FORKLIFT APP VIEWS
from .views import equipment_index

#URL PATTERNS
urlpatterns = [
    #URL PATTERN INDEX
    path('', equipment_index, name='forklift_index_view'),
]