from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionManager,
    BaseUserManager,
)


class MiUserManager(BaseUserManager):
    def _create_user(
        self,
        username,
        password,
        email,
        first_name,
        last_name,
        telefono,
        image,
        disponible,
        session_token,
        **extra_fields
    ):
        if not username:
            raise ValueError("erroooorrrr usuarioo")
        if not password:
            raise ValueError("erroooorrrr passssss")
        user = self.model(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            telefono=telefono,
            image=image,
            disponible=disponible,
            session_token=session_token,
            **extra_fields
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_user(
        self,
        username,
        email,
        password,
        first_name,
        last_name,
        telefono,
        image,
        disponible,
        session_token,
        **extra_fields
    ):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(
            username,
            email,
            password,
            first_name,
            last_name,
            telefono,
            image,
            disponible,
            session_token,
        )

    def create_superuser(
        self,
        username,
        email,
        password,
        first_name,
        last_name,
        telefono,
        image,
        disponible,
        session_token,
        **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(
            username,
            email,
            password,
            first_name,
            last_name,
            telefono,
            image,
            disponible,
            session_token,
        )


class User(AbstractBaseUser, PermissionManager):
    username = models.CharField(db_index=True, unique=True, max_length=255)
    email = models.EmailField(
        db_index=True,
        unique=True,
        null=False,
        max_length=255,
        default="default@example.com",
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    telefono = models.CharField(max_length=8, unique=True)
    image = models.TextField(null=True, blank=True)
    disponible = models.BooleanField(default=False, null=True)
    session_token = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = MiUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "password",
        "telefono",
        "first_name",
        "last_name",
        "username",
    ]


class Roles(models.Model):
    nombre = models.CharField(max_length=255, null=False, unique=True)
    image = models.CharField(max_length=255, null=True)
    ruta = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class UserHasRol(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="roles")
    rol = models.ForeignKey(Roles, on_delete=models.CASCADE, related_name="users")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "rol"], name="unique_user_role")
        ]
