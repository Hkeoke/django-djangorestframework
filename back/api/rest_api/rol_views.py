from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from api.models import Roles, User, UserHasRol


class RolesbyUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.data.get("user_id")
        if user_id is None:
            return Response(
                {"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        roles = self.get_roles_for_user(user_id)
        return Response(roles, status=status.HTTP_200_OK)

    def get_roles_for_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        user_roles = user.roles.all()
        roles_list = [
            {"rol_id": user_role.rol.id, "nombreRol": user_role.rol.nombre}
            for user_role in user_roles
        ]

        return roles_list


class UsersbyRoleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        rol_id = request.data.get("rol_id")  # Solo tomamos el rol_id

        if rol_id is None:
            return Response(
                {"error": "rol_id is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        return self.get_users_for_role(rol_id)

    def get_users_for_role(self, rol_id):
        try:
            role = Roles.objects.get(id=rol_id)  # Obtener el rol
        except Roles.DoesNotExist:
            return Response(
                {"error": "Role not found"}, status=status.HTTP_404_NOT_FOUND
            )

        users_with_role = UserHasRol.objects.filter(
            rol=role
        )  # Obtener usuar con este rol
        user_list = [
            {"user_id": user_has_rol.user.id, "username": user_has_rol.user.username}
            for user_has_rol in users_with_role
        ]

        return Response({"users": user_list}, status=status.HTTP_200_OK)
