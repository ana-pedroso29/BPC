from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('busca_bpc.urls')), # Inclui as URLs do nosso aplicativo
]