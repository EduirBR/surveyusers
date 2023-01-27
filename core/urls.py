from django.contrib import admin
from django.urls import path, include
from apps.countries.views import CountryUserview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('countries/', include('apps.countries.urls')),
    path('biome/', include('apps.bioma.urls')),
    # path('gg/', CountryUserview.)
]
