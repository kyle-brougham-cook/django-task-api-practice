import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

@pytest.fixture
def test_user():
    return User.objects.create_user(
        username="testuser",
        email="test@example.com",
        password="strongpass123"
    )


@pytest.fixture
def loggedin_user(test_user):
    client = APIClient()
    client.force_login(user=test_user)
    return client


@pytest.fixture
def user_factory():
    def create_user(username="default", email="default@example.com", password="defaultpass"):
        return User.objects.create_user(username=username, email=email, password=password)
    return create_user
