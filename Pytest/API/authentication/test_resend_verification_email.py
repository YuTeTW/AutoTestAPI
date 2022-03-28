from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
url = URL + "/auth/resend_verification_email"

login_data = {
    "email": "judhaha@gmail.com",
    "password": "dave"
}

# def test_resend_email_success():
#     default_DB.default()
#
#     create_new_user()
#     Login_new_user()
#     url = URL + "/users/verify_code_enable"
#     client.patch(url, headers=get_current_user_header(), params="verify_code_enable=1")
#     Login_new_user()
#     with open(os.getcwd()+ '/Pytest/Default/User_data/verify_code.txt',
#               'r', encoding="utf-8") as token_data:
#         token = token_data.read()
#
#     url = URL + "/auth/login/verify_code"
#     client.post(url, json=login_data, params="verify_code=" + str(token))
#     Login_new_user()
#     url = URL + "/users/verify_code_enable"
#     client.patch(url, headers=get_current_user_header(), params="verify_code_enable=0")
#
#     request.post(url, 200, validate_response="ResendVerificationEmail Done"
#                  ,params={"email" : "Test_RD@fastwise.net"})
