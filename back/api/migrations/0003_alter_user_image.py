# Generated by Django 5.1 on 2024-08-26 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_roles_userhasrol"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="image",
            field=models.TextField(blank=True, null=True),
        ),
    ]
