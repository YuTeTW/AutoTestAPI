from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
url = URL + "/users/email/exists"


def test_check_email_exist():
    default_DB.default()
    request.get(url, 200, validate_response="Email is exist", params="email=Test_RD@fastwise.net")


def test_check_email_exist_fail():
    default_DB.default()
    request.get(url, 404, validate_response={'detail': 'Email does not exist'}, params="email=abc@fastwise.net")