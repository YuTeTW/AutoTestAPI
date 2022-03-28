from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
url = URL + "/users/verify_code_enable"


# def test_patch_user_verify_code_enable_HR():
#     default_DB.default()
#     Login_HR()
#     request.patch(url, 200, headers=get_current_user_header(), params="verify_code_enable=0")

def test_patch_user_verify_code_enable_normal_user():
    default_DB.default()
    Login_normal_user()
    request.patch(url, 200, headers=get_current_user_header(), params="verify_code_enable=1")
