import pytest
@pytest.fixture
def sample_user():
    return {
        "username": "testuser",
        "email": "test@example.com"
    }
def test_user_has_email(sample_user):
    assert "email" in sample_user
