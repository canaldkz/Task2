from faker import Faker
import pytest



@pytest.fixture(scope='session')
def faker():
    return Faker()


@pytest.fixture
def random_user(request):
    faker = Faker()
    request.cls.login = faker.email() # Generate Login
    request.cls.password = faker.password() # Generate Password