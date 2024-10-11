"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from dashboard.views import index
from visitantes.views import registrar_visitante, finalizar_visita, informacoes_visitante
from moradores.views import lista_moradores
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name= 'index'),
    path('registrar_visitante/', registrar_visitante, name='registrar_visitante'),
    path('login/', LoginView.as_view(template_name='login.html'), name= 'login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name= 'logout'),

    path('visitante/<int:pk>/',informacoes_visitante, name='informacoes_visitante'),
    path('visitante/<int:pk>/finalizar-visita',finalizar_visita, name='finalizar_visita'),

    path('api/', include('api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('lista_moradores/', lista_moradores, name='lista_moradores'),
]
