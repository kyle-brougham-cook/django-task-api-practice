import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from tests.utils import get_access_token, create_new_task

@pytest.mark.django_db
def test_get_all_user_tasks(loggedin_user):
    client = APIClient()
    url = reverse("task-list")

    token = get_access_token(client, "testuser", "strongpass123")
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    create_new_task(client)

    response = client.get(
        url, format="json")

    assert response.status_code == 200 # type: ignore
    assert response.data[0]["title"] == "test" # type: ignore
    assert response.data[0]["description"] == "testtask" # type: ignore



@pytest.mark.django_db
def test_post_new_user_task(loggedin_user):
    client = APIClient()
    url = reverse("task-list")

    token = get_access_token(client, "testuser", "strongpass123")
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    response = client.post(
        url, {
            "title": "test",
            "description": "testtask"
        }, format="json")

    assert response.status_code == 201 # type: ignore
    assert response.data["title"] == "test" # type: ignore
    assert response.data["description"] == "testtask" # type: ignore