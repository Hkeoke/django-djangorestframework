"""
URL configuration for back project.

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

from django.urls import path, include
from django.views.generic import TemplateView

from api.rest_api.auth_views import LoginView, LogoutView
from api.rest_api.views import UserViewSet
from api.rest_api.rol_views import RolesbyUserView, UsersbyRoleView
from api import views


urlpatterns = [
    path("api/", include("api.rest_api.urls")),
    path("api/login/", LoginView.as_view(), name="api_login"),
    path("api/logout/", LogoutView.as_view(), name="api_logout"),
    path(
        "api/usuarios/",
        UserViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="usuarios",
    ),
    path("api/rolesbyuser/", RolesbyUserView.as_view(), name="user_roles"),
    path("api/usersbyrol/", UsersbyRoleView.as_view(), name="roles_user_view"),
    path("login/", views.loginView, name="login"),
    path("create/", views.createView, name="create"),
    path("upload_image/", views.upload_image, name="upload_image"),
    path("principal/", views.principalpageView, name="principal"),
    path("logout/", views.logoutView, name="logout"),
]
