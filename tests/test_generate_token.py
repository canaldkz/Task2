import httpx


def test_token():
    body = {"userName": "i@mmmalikov.ru", "password": "Zzzz123!"}
    response = httpx.post("https://demoqa.com/Account/v1/GenerateToken", json=body)

    assert response.status_code == 200
    assert response.json().get("status") == "Success"

def test_token_incorrect_password():
    body = {"userName": "i@malikov.ru", "password": "Zzzz123"}
    response = httpx.post("https://demoqa.com/Account/v1/GenerateToken", json=body)

    assert response.status_code == 200
    assert response.json().get("status") == "Failed"
    assert response.json().get("token") == None
