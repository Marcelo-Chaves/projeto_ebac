from django.contrib import admin
from django.urls import path, include  # Use 'include' para incluir as URLs do app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('app_ebac.urls')),
    path('', include('app_ebac.urls')),
]
