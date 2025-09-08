import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from tests.utils import get_access_token, create_new_task


@pytest.mark.django_db
def test_get_user_task_details_success(loggedin_user):
    client = APIClient()

    token = get_access_token(client, "testuser", "strongpass123")
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    task_id = create_new_task(client)["id"]

    url = reverse("task-detail", args=[task_id])
    response = client.get(url, format="json")
    assert response.status_code == 200 # type: ignore
    assert response.data["title"] == "test" # type: ignore


@pytest.mark.django_db
def test_delete_user_task_success(loggedin_user):
    client = APIClient()

    token = get_access_token(client, "testuser", "strongpass123")
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    task_id = create_new_task(client)["id"]

    url = reverse("task-detail", args=[task_id])
    response = client.delete(url, format="json")
    assert response.status_code == 204 # type: ignore


@pytest.mark.django_db
def test_put_user_task_success(loggedin_user):
    client = APIClient()

    token = get_access_token(client, "testuser", "strongpass123")
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    task_id = create_new_task(client)["id"]

    url = reverse("task-detail", args=[task_id])
    response = client.put(url, {
        "title": "newTask",
        "description": "newTestTask"
    }, format="json")

    assert response.status_code == 200 # type: ignore
    assert response.data["title"] == "newTask" # type: ignore
    assert response.data["description"] == "newTestTask" # type: ignore


@pytest.mark.django_db
def test_patch_user_task_success(loggedin_user):
    client = APIClient()

    token = get_access_token(client, "testuser", "strongpass123")
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    task_id = create_new_task(client)["id"]

    url = reverse("task-detail", args=[task_id])
    response = client.patch(url, {
        "title": "newTask"
    }, format="json")

    assert response.status_code == 200 # type: ignore
    assert response.data["title"] == "newTask" # type: ignore
    assert response.data["description"] == "testtask" # type: ignore