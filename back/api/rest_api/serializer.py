from rest_framework import serializers
from api.models import User, Roles, UserHasRol


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "telefono",
            "image",
            "session_token",
            "disponible",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {"password": {"write_only": True}}

        read_only_fields = [
            "id",
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        default_image = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAM1BMVEXk5ueutLeqr7HKzc/j5ebW2Nv2+Pnc4OJmamp6foGNkZRna2xVWFxOUlVYXWFla2xuXU5D5XIVAAAFDklEQVR4nO2d2bLbIAxAbYE3sDH//7WFbPfexG4MiCAcnWmnrzkjIRaD2jQMwzAMwzAMwzAMwzAMwzAMwzAMwzAMwzAMwzAMw5wQkHJczewxZh2lhNK/CBOQUrKzLCYQSii/Qiige0VsLeU7yprrjRDOlfgRQkae/JCzie6El9JuEPjBYwROjHQdb4Rwq8QTFwqgRwiHSjxgoQB1hHAkPsNCAdoIYSLxgIUC9BDCjBIHWCiAGSHMKfGChQLDhDBWiRohdalr8rY7Wmm6EEI9pVkYwXEt/4WE0NQxUsT1CwdCCDlVhYDi8JEaQqinTxVXH/kIIVxM33Hv0rijSAihstoJLRxIRwiVfa3vu5asQgghe08Pg9IdBEIIkZbF9Ri6EvVDCD/Jln0Mt1LDh2gIIWLbie0xZKellBDCQm2TKveGDRBCMZH37jDv2+Uw101pIYSTbIwXbUGvHAZCCGFhRvcQ35TNh4ESQmjZ"
        if "image" not in validated_data or validated_data["image"] is None:
            validated_data["image"] = default_image

        user.save()
        default_role = Roles.objects.get(id=1)  # pra asignar rol por defecto
        UserHasRol.objects.create(user=user, rol=default_role)
        return user


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ["id", "nombre", "image", "ruta", "created_at", "updated_at"]


class UserHasRolSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHasRol
        fields = ["rol_id", "user_id", "created_at", "updated_at"]
