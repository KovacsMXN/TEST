#INCLUDE
from django.urls import path, include

#INCLUDE LADDERS APP VIEWS
from .views import ladders_index

#URL PATTERNS
urlpatterns = [
    #URL PATTERN INDEX
    path('', ladders_index, name='ladders_index_view'),
]