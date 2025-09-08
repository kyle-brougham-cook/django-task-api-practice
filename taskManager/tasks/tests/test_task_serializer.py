import pytest
from django.urls import reverse
from tests.utils import get_access_token
from tasks.serializer import TaskSerializer
from rest_framework.test import APIClient, APIRequestFactory


def get_mock_request(user):
    factory = APIRequestFactory()
    request = factory.post("/tasks/")
    request.user = user
    return request


@pytest.mark.django_db
def test_user_task_seralizer_empty_description_no_api_denial(test_user):
    request = get_mock_request(test_user)

    data = {
        "title": "test",
        "description": " ",
        "done": True
    }

    serializer = TaskSerializer(data=data, context={"request": request})
    assert not serializer.is_valid()
    assert "Description cannot be empty or whitespace" in serializer.errors["description"][0] # type: ignore


@pytest.mark.django_db
def test_user_task_seralizer_not_bool_no_api_denial(test_user):
    request = get_mock_request(test_user)

    data = {
        "title": "test",
        "description": "testuserdescription",
        "done": " "
    }

    serializer = TaskSerializer(data=data, context={"request": request})
    assert not serializer.is_valid()
    assert "Must be a valid boolean" in serializer.errors["done"][0] # type: ignore


@pytest.mark.django_db
def test_user_task_serializer_empty_description_denial(loggedin_user):
    client = APIClient()
    token = get_access_token(client, "testuser", "strongpass123")
    url = reverse("task-list")


    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    response = client.post(
        url, {
            "title": "test",
            "description": " "
        }, format="json"
    )


    assert response.status_code == 400 # type: ignore
    assert "Description cannot be empty or whitespace" in response.data["description"][0] or "This field may not be blank." in response.data["description"][0] # type: ignore


@pytest.mark.django_db
def test_user_task_serializer_empty_title_denial(loggedin_user):
    client = APIClient()
    token = get_access_token(client, "testuser", "strongpass123")
    url = reverse("task-list")


    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    response = client.post(
        url, {
            "title": " ",
            "description": "testusertask"
        }, format="json"
    )


    assert response.status_code == 400 # type: ignore
    assert "Title cannot be empty or whitespace" in response.data["title"][0] or "This field may not be blank." in response.data["title"][0] # type: ignore


@pytest.mark.django_db
def test_user_task_serializer_short_description_denial(loggedin_user):
    client = APIClient()
    token = get_access_token(client, "testuser", "strongpass123")
    url = reverse("task-list")


    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    response = client.post(
        url, {
            "title": "test",
            "description": "testtask"
        }, format="json"
    )


    assert response.status_code == 400 # type: ignore
    assert "Description cant be less than 10 characters in length" in response.data["description"][0] or "Ensure this field has at least 10 characters." in response.data["description"][0] # type: ignore



@pytest.mark.django_db
def test_user_task_serializer_long_description_denial(loggedin_user):
    client = APIClient()
    token = get_access_token(client, "testuser", "strongpass123")
    url = reverse("task-list")


    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    response = client.post(
        url, {
            "title": "test",
            "description": "testusertaskkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
        }, format="json"
    )


    assert response.status_code == 400 # type: ignore
    assert "Description cannot be more than 150 characters in length" in response.data["description"][0] or "Ensure this field has no more than 150 characters." in response.data["description"][0] # type: ignore



@pytest.mark.django_db
def test_user_task_serializer_long_title_denial(loggedin_user):
    client = APIClient()
    token = get_access_token(client, "testuser", "strongpass123")
    url = reverse("task-list")


    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    response = client.post(
        url, {
            "title": "testusertitleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
            "description": "testusertask"
        }, format="json"
    )


    assert response.status_code == 400 # type: ignore
    assert "Title cannot be empty or whitespace" in response.data["title"][0] or "Ensure this field has no more than 50 characters." in response.data["title"][0] # type: ignore


@pytest.mark.django_db
def test_user_task_serializer_empty_done_denial(loggedin_user):
    client = APIClient()
    token = get_access_token(client, "testuser", "strongpass123")
    url = reverse("task-list")


    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    response = client.post(
        url, {
            "title": "test",
            "description": "testusertask",
            "done": "random"
        }, format="json"
    )


    assert response.status_code == 400 # type: ignore
    assert "Done must be either true or false" in response.data["done"][0] or "Must be a valid boolean." in response.data["done"][0] # type: ignore
