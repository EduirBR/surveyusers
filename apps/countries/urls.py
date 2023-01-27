from apps.countries.views import CountriesViewSet,CountryUserview
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register('something/', CountryUserview )
# router.register('', CountriesViewSet )
urlpatterns =[
]

urlpatterns += router.urls