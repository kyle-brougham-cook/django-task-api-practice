import pytest
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.mark.django_db
def test_user_login_success(test_user):
    client = APIClient()
    url = reverse("token_obtain_pair")

    payload = {
        "username": "testuser",
        "password": "strongpass123"
    }

    response = client.post(url, payload, format="json")

    assert response.status_code == 200 # type: ignore
    assert "access" in response.data # type: ignore
    assert "refresh" in response.data # type: ignore


@pytest.mark.django_db
def test_user_login_no_user(test_user):
    client = APIClient()
    url = reverse("token_obtain_pair")

    payload = {
        "username": "incorrecttestuser",
        "password": "strongpass123"
    }

    response = client.post(url, payload, format="json")

    assert response.status_code == 401 # type: ignore
    assert "detail" in response.data # type: ignore
    assert response.data["detail"] == "No active account found with the given credentials" # type: ignore


@pytest.mark.django_db
def test_user_login_wrong_password(test_user):
    client = APIClient()
    url = reverse("token_obtain_pair")

    payload = {
        "username": "testuser",
        "password": "incorrectpass123"
    }

    response = client.post(url, payload, format="json")

    assert response.status_code == 401 # type: ignore
    assert "detail" in response.data # type: ignore
    assert response.data["detail"] == "No active account found with the given credentials" # type: ignore


    