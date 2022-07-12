import pytest
from fastapi.testclient import TestClient

from presentation.const import API_PREFIX
from presentation.main import app

client = TestClient(app)

API_COUNTRY_TEST_DATA = [("HR", "10000", 200, "Croatia")]


@pytest.mark.parametrize(
    "country_code, postal_code, expected_status, expected_country",
    API_COUNTRY_TEST_DATA,
)
def test_api_country_code(country_code, postal_code, expected_status, expected_country):
    url = f"{API_PREFIX}/{country_code}/{postal_code}"
    response = client.get(url=url)
    assert response.status_code == expected_status
    response_body = response.json()
    assert response_body["country"] == expected_country


def test_api_country_code_mocked(mocker):
    mocker.patch("requests.get", return_value=...)
