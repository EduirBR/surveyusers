from django.contrib import admin
from django.urls import path, include
from apps.countries.views import fill

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('countries/', include('apps.countries.urls')),
    ##path('', fill)

]
