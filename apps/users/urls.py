from apps.users.views import UserView
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register('', UserView )
urlpatterns =[
]

urlpatterns += router.urls
