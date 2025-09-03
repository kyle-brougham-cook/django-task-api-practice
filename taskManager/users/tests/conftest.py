import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def test_user():
    return User.objects.create_user(
        username="testuser",
        email="test@example.com",
        password="strongpass123"
    )