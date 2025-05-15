from django.urls import path
from . import views

urlpatterns = [
    path('buscar/', views.formulario_busca, name='formulario_busca'),
    path('resultados/', views.exibir_resultados, name='exibir_resultados'),
    path('get_cidades/<str:sigla_estado>/', views.get_cidades_por_estado, name='get_cidades_por_estado'), # Nova URL
]