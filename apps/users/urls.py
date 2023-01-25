from apps.users.views import UserView, UserREAD
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register('', UserView )
router.register('/tt', UserREAD )
urlpatterns =[
]

urlpatterns += router.urls
