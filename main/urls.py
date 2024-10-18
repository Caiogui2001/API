from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet , FuncionarioViewSet

router = DefaultRouter()
router.register(r'item', ItemViewSet)

router = DefaultRouter()
router.register(r'funcionario', FuncionarioViewSet)

urlpatterns = [
    path('', include(router.urls))
]

