from rest_framework import routers
from django.urls import include, path

from api.viewsets import UsuarioViewSet, VisitanteViewSet, PorteiroViewSet

router = routers.DefaultRouter()

router.register(r'usuarios', UsuarioViewSet)
router.register(r'visitantes', VisitanteViewSet)
router.register(r'porteiros', PorteiroViewSet)

urlpatterns = [
    path('', include(router.urls))
]