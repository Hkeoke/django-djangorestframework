from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.rest_api.views import UserViewSet, RolesViewSet, UserHasRolViewSet


router = DefaultRouter()
router.register("usuarios", UserViewSet, basename="user")
router.register("roles", RolesViewSet, basename="rol")
router.register("has_roles", UserHasRolViewSet, basename="has_rol")
urlpatterns = router.urls
