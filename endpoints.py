def test_get_users_returns_empty_list(client):
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == []
