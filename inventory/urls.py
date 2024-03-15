#INCLUDE
from django.urls import path, include

#INCLUDE INVENTORY APP VIEWS
from .views import stock_index

#INCLUDE STOCK MOTORS
from .views import stock_motors_index, stock_motorsbrands_index

#URL PATTERNS
urlpatterns = [
    #URL PATTERN INDEX
    path('', stock_index, name='stock_index'),

    #URLS APP MOTORS
    #URLS MOTORS INDEX 
    path('motors/', stock_motors_index, name='stock_motors_index'),
    #URLS MOTORS BRANDS INDEX
    path('motors/brands/', stock_motorsbrands_index, name='stock_motorsbrands_index'),

]