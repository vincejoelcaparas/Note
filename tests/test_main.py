from app.main import app


def test_create_note():
    client = app.test_client()
    response = client.post("/notes", json={"text": "Learn DevOps"})
    assert response.status_code == 201
    assert response.get_json()["text"] == "Learn DevOps"


def test_get_notes():
    client = app.test_client()
    client.post("/notes", json={"text": "Test Note"})
    response = client.get("/notes")
    assert response.status_code == 200
    assert len(response.get_json()) > 0
