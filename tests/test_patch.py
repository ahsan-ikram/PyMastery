from unittest.mock import patch

import requests
from requests import Response


def third_party_dependency() -> int:
    url = "https://www.google.com"
    try:
        response: Response = requests.get(url, timeout=2.50)
        return response.status_code
    except requests.exceptions.HTTPError as http_error:
        print("Http Error:", http_error)
    except requests.exceptions.ConnectionError as connection_error:
        print("Error Connecting:", connection_error)
    except requests.exceptions.Timeout as timeout_error:
        print("Timeout Error:", timeout_error)
    except requests.exceptions.RequestException as request_error:
        print("Oh No!: Something Else", request_error)
    return -1


def api_response() -> str:
    return "success" if third_party_dependency() == 200 else "failure"


@patch("tests.usecases.third_party_dependency")
def test_api_response(mocker):
    mocker.return_value = 200
    assert api_response() == "success"
