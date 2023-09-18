import httpx

def test_autorization():
    body = {"userName": "i@mmmalikov.ru", "password": "Zzzz123!"}
    response = httpx.post("https://demoqa.com/Account/v1/Authorized", json=body)

    assert response.status_code == 200

def test_incorrect_username():
    body = {"userName": "imalikov.ru", "password": "Zzzz123!"}
    response = httpx.post("https://demoqa.com/Account/v1/Authorized", json=body)

    assert response.status_code == 404
    assert response.json().get("code") == "1207"
    assert response.json().get("message") == "User not found!"

def test_incorrect_password(faker):
    body = {"userName": "i@malikov.ru", "password": "Zzzz123"}
    response = httpx.post("https://demoqa.com/Account/v1/Authorized", json=body)

    assert response.status_code == 404
    assert response.json().get("code") == "1207"
    assert response.json().get("message") == "User not found!"