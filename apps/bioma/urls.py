from rest_framework.routers import DefaultRouter
from apps.bioma.views import BiomeViewSet
router = DefaultRouter(trailing_slash=False)
router.register('', BiomeViewSet )
urlpatterns =[
]

urlpatterns += router.urls