from unittest.mock import patch
from tests.usecases import api_response


@patch("tests.usecases.third_party_dependency")
def test_api_response(mocker):
    mocker.return_value = 200
    assert api_response() == "success"
