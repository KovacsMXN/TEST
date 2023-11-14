#INCLUDE
from django.urls import path, include

from .views import api_pull_forklifts, api_pull_holders, api_pull_serviceproviders, api_pull_brands,api_del_forklifts, api_pull_experimental

#URL PATTERNS
urlpatterns = [
    #API PULL FORKLIFTS
    path('pull/forklifts/', api_pull_forklifts, name='api_pull_forklifts'),
    path('delete/forklifts/<int:id>', api_del_forklifts, name='api_del_forklifts'),
    path('pull/holders/', api_pull_holders, name='api_pull_holders'),
    path('pull/serviceproviders/', api_pull_serviceproviders, name='api_pull_serviceproviders'),
    path('pull/brands/', api_pull_brands, name='api_pull_brands'),
    path('pull/experimental/<int:id>', api_pull_experimental, name='api_pull_experimentl'),
]