import pytest
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.mark.django_db
def test_user_registration_returns_tokens():
    client = APIClient()
    url = reverse("register")

    payload = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "strongpass123"
    }

    response = client.post(url, payload, format="json")

    assert response.status_code == 201 # type: ignore
    assert "access" in response.data # type: ignore
    assert "refresh" in response.data  # type: ignore


@pytest.mark.django_db
def test_user_registration_missing_data():
    client = APIClient()
    url = reverse("register")

    payload = {
        "username": "testuser",
        "email": "test@example.com",
        "password": ""
    }

    response = client.post(url, payload, format="json")

    assert response.status_code == 400 # type: ignore
    assert "password" in response.data # type: ignore
    assert response.data["password"][0] == "This field may not be blank." # type: ignore



@pytest.mark.django_db
def test_user_registration_short_password():
    client = APIClient()
    url = reverse("register")


    payload = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "123"
    }

    response = client.post(url, payload, format="json")

    assert response.status_code == 400 # type: ignore
    assert "This password is too short." in response.data["password"][0] # type: ignore


@pytest.mark.django_db
def test_user_registration_invalid_email():
    client = APIClient()
    url = reverse("register")

    payload = {
        "username": "testuser",
        "email": "test@example",
        "password": "strongpass123"
    }

    response = client.post(url, payload, format="json")

    assert response.status_code == 400  # type: ignore
    assert "email" in response.data # type: ignore
    assert response.data["email"][0] == "Enter a valid email address." # type: ignore




@pytest.mark.django_db
def test_user_registration_email_in_use(test_user):
    client = APIClient()
    url = reverse("register")

    payload = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "strongpass123"
    }

    response = client.post(url, payload, format="json")

    assert response.status_code == 400 # type: ignore
    assert "email" in response.data # type: ignore
    assert response.data["email"][0] == "This field must be unique." # type: ignore




@pytest.mark.django_db
def test_user_registration_username_in_use(test_user):
    client = APIClient()
    url = reverse("register")

    payload = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "strongpass123"
    }

    response = client.post(url, payload, format="json")

    assert response.status_code == 400 # type: ignore
    assert "username" in response.data # type: ignore
    assert response.data["username"][0] == "This field must be unique." # type: ignore








