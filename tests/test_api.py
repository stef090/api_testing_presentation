import pytest
from fastapi.testclient import TestClient

from presentation.const import API_PREFIX
from presentation.main import app

client = TestClient(app)


class MockResponse:
    def __init__(self, url):
        self.url = url


API_COUNTRY_TEST_DATA = [
    ("HR", "10000", 200, "Croatia", "http://bla"),
    # ("HR", "50000", 404, None, "http://bla"),
]


@pytest.mark.parametrize(
    "country_code, postal_code, expected_status, expected_country, url",
    API_COUNTRY_TEST_DATA,
)
def test_api_country_code(
    country_code, postal_code, expected_status, expected_country, url
):
    mock = MockResponse(url=url)
    url = f"{API_PREFIX}/{country_code}/{postal_code}"
    response = client.get(url=url)
    assert response.status_code == expected_status
    response_body = response.json()
    assert response_body.get("country") == expected_country


def test_api_country_code_mocked(mocker):
    mocker.patch("requests.get", return_value=...)
