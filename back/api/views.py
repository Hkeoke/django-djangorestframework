import base64
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse
from api.httprequest import createUser

from rest_framework import status


from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from api.models import (
    User,
    UserHasRol,
)


def loginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            try:
                user = User.objects.get(username=username)

                if user.check_password(password):
                    login(request, user)
                    return redirect("principal")
                else:
                    return render(
                        request,
                        "loguin.html",
                        {"error": "Usuario or contrasenna no validos."},
                    )
            except User.DoesNotExist:
                return render(
                    request,
                    "loguin.html",
                    {"error": "Usuario or contrasenna no validos."},
                )
        else:
            return render(
                request,
                "loguin.html",
                {"error": "Usuario y contrasenna son requeridos."},
            )
    return render(request, "loguin.html")


def createView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        telefono = request.POST.get("telefono")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        if username and email and password and telefono and first_name and last_name:
            response = createUser(
                username, email, password, telefono, first_name, last_name
            )
            if response.status_code == status.HTTP_201_CREATED:
                return redirect("login")
            else:
                return render(request, "create.html", {"error": response.data["error"]})
        else:
            return render(
                request, "create.html", {"error": "Todos los campos son requeridos."}
            )
    return render(request, "create.html")


@login_required
def principalpageView(request):
    user = request.user
    user_roles = UserHasRol.objects.filter(user=user).select_related("rol")
    roles = [user_role.rol for user_role in user_roles]

    context = {
        "user": user,
        "roles": roles,
    }
    return render(request, "principalpage.html", context)


@login_required
def upload_image(request):
    if request.method == "POST":
        file = request.FILES.get("file")
        if file:
            try:
                image_data = base64.b64encode(file.read()).decode("utf-8")
                request.user.image = image_data
                request.user.save()
                return redirect("principal")
            except Exception as e:
                return render(request, "principalpage.html")
        else:
            return render(request, "principalpage.html")
    else:
        return render(request, "principalpage.html")


@login_required
def logoutView(request):
    logout(request)
    return redirect(reverse("login"))
