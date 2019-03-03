from django.urls import path, include
from rest_framework.routers import DefaultRouter

from categories.api import CategoryViewSet

# Creamos un router
router = DefaultRouter()

# Si tenemos definido un atributo queryset en el QuerySet no hace falta poner base_name=' ...'
router.register('categories', CategoryViewSet)

urlpatterns = [
    # API REST
    path('api/1.0/', include(router.urls))
]
