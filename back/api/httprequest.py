import json
from django.urls import reverse
import requests
from django.conf import settings


def make_login_request(username, password):
    url = reverse("api_login")
    data = {"username": username, "password": password}
    headers = {"Content-Type": "application/json"}

    response = requests.post(
        settings.API_BASE_URL + url, data=json.dumps(data), headers=headers
    )
    return response


def createUser(username, email, password, telefono, first_name, last_name):
    url = reverse("usuarios")
    data = {
        "username": username,
        "email": email,
        "password": password,
        "telefono": telefono,
        "first_name": first_name,
        "last_name": last_name,
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        settings.API_BASE_URL + url, data=json.dumps(data), headers=headers
    )

    return response
