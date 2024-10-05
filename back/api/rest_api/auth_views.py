from api.models import User
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.exceptions import InvalidToken

from api.rest_api.rol_views import RolesbyUserView


class LoginView(APIView):
    def post(self, request):

        username_or_email = request.data.get("username")
        password = request.data.get("password")

        print("llego peticion")

        User = get_user_model()

        try:
            if "@" in username_or_email:  # si es con un '@' es un email
                user = User.objects.get(email=username_or_email)
            else:
                user = User.objects.get(username=username_or_email)

            if user.check_password(password):
                tokens = get_tokens_for_user(user)

                return Response(tokens, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": "Credenciales inválidas"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        except User.DoesNotExist:
            return Response(
                {"error": "Credenciales inválidas"},
                status=status.HTTP_401_UNAUTHORIZED,
            )


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    rol_view = RolesbyUserView()
    rol = rol_view.get_roles_for_user(user.id)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "userId": user.id,
        "roles": rol,
    }


class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh")
        if refresh_token is None:
            return Response(
                {"error": "Se requiere el refresh token."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()  # blokear token

            return Response(
                {"detail": "Cierre de sesión exitoso."}, status=status.HTTP_200_OK
            )
        except InvalidToken:
            return Response(
                {"error": "Token inválido."}, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
