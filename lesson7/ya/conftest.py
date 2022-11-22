import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="Url for test api location"
    )

    parser.addoption(
        "--status_code",
        default=200,
        help="Success response"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")
