import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data

def test_signup_and_unregister():
    # Use a unique email to avoid conflicts
    test_email = "pytestuser@mergington.edu"
    activity = "Chess Club"
    # Signup
    signup_resp = client.post(f"/activities/{activity}/signup?email={test_email}")
    assert signup_resp.status_code == 200 or signup_resp.status_code == 400  # 400 if already signed up
    # Unregister
    unregister_resp = client.delete(f"/activities/{activity}/unregister?email={test_email}")
    assert unregister_resp.status_code == 200 or unregister_resp.status_code == 404  # 404 if not found
