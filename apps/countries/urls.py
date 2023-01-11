from apps.countries.views import CountriesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register('', CountriesViewSet )
urlpatterns =[
]

urlpatterns += router.urls