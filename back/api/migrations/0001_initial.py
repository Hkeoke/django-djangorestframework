# Generated by Django 5.1 on 2024-08-19 13:25

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "username",
                    models.CharField(db_index=True, max_length=255, unique=True),
                ),
                (
                    "email",
                    models.EmailField(
                        db_index=True,
                        default="default@example.com",
                        max_length=255,
                        unique=True,
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("telefono", models.CharField(max_length=8, unique=True)),
                ("image", models.CharField(max_length=255, null=True)),
                ("disponible", models.BooleanField(default=False, null=True)),
                ("session_token", models.CharField(max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("is_staff", models.BooleanField(default=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_superuser", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
            bases=(models.Model, django.contrib.auth.models.PermissionManager),
        ),
    ]
