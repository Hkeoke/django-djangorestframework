from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models import User
from api.models import Roles
from api.models import UserHasRol
from api.rest_api.serializer import UserSerializer
from api.rest_api.serializer import RolesSerializer
from api.rest_api.serializer import UserHasRolSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        """
        instancio y  devuelvo la  lista de permissions que esta view requiere
        """
        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    permission_classes = [IsAuthenticated]


class UserHasRolViewSet(viewsets.ModelViewSet):
    queryset = UserHasRol.objects.all()
    serializer_class = UserHasRolSerializer
    permission_classes = [IsAuthenticated]
