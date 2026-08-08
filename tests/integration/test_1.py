from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch
client = TestClient(app)

def test_routes():
    
    response = client.post("/login", json={"email": "testuser@example.com", "password": "testpassword"})
    versions=client.delete("/documents/1", headers={"Authorization": f"Bearer {response.json()['access_token']}"})
    assert versions.status_code == 200