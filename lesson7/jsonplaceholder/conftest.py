import pytest


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url", default='https://jsonplaceholder.typicode.com')
