#INCLUDE GENERIC
from django.urls import path, include

#INCLUDE FORKLIFTS
from .views import api_pull_forklifts
from .views import api_del_forklifts

#INCLUDE HOLDERS
from .views import api_pull_holders
from .views import api_del_forkliftowners

#INCLUDE SERVICE PROVIDERS
from .views import api_pull_serviceproviders
from .views import api_del_forklifts_service_provider

#INCLUDE BRANDS
from .views import api_pull_brands
from .views import api_del_forklifts_brands

#INCLUDE STATUS
from .views import api_pull_status
from .views import api_del_forklifts_status

#URL PATTERNS
urlpatterns = [

#FORKLIFTS
    path('pull/forklifts/', api_pull_forklifts, name='api_pull_forklifts'),
    path('delete/forklifts/<int:id>/', api_del_forklifts, name='api_del_forklifts'),

#HOLDERS
    path('pull/holders/', api_pull_holders, name='api_pull_holders'),
    path('delete/forkliftsowners/<int:id>/', api_del_forkliftowners, name='api_del_forkliftowners'),

#SERVICE PROVIDERS
    path('pull/serviceproviders/', api_pull_serviceproviders, name='api_pull_serviceproviders'),
    path('delete/serviceproviders/<int:id>/', api_del_forklifts_service_provider, name='api_del_forklifts_service_provider'),

#BRANDS
    path('pull/brands/', api_pull_brands, name='api_pull_brands'),
    path('delete/brands/<int:id>/', api_del_forklifts_brands, name='api_del_forklifts_brands'),

#STATUS
    path('pull/status/<int:id>/', api_pull_status, name='api_pullstatus'),
    path('delete/status/<int:id>/', api_del_forklifts_status, name='api_del_forklifts_status'),
]