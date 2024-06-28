from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PessoaViewSet, SetorViewSet

router = DefaultRouter()
router.register(r'pessoa', PessoaViewSet)
router.register(r'setor', SetorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]