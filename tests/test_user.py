import httpx
import pytest


@pytest.mark.usefixtures("random_user")
class TestUser:
    def test_user_post(self):
        print(self.login)
        response = httpx.post(
            "https://demoqa.com/Account/v1/User",
            json={"userName": self.login, "password": self.password},
        )

        assert response.status_code == 201

    def test_user_exists(self):
        print(self.login)
        response = httpx.post(
            "https://demoqa.com/Account/v1/User",
            json={"userName": self.login, "password": self.password},
        )

        assert response.status_code == 406
        assert response.json().get("message") == "User exists!"
        assert response.json().get("code") == "1204"
