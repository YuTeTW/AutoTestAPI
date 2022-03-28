from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
url = URL + "/auth/login/verify_code"
with open(os.getcwd() + "/Pytest/API/validate_staff_schema.json", encoding="utf-8") as json_file:
    validate_schema = json.load(json_file)

login_data = {
    "email": "judhaha@gmail.com",
    "password": "dave"
}

def test_login_step2():
    default_DB.default()
    create_new_user()
    Login_new_user()
    url = URL + "/users/verify_code_enable"
    client.patch(url, headers=get_current_user_header(), params="verify_code_enable=1")

    Login_new_user()
    with open(os.getcwd()+ '/Pytest/Default/User_data/verify_code.txt',
              'r', encoding="utf-8") as token_data:
        token = token_data.read()

    url = URL + "/auth/login/verify_code"
    request.post(url, 200, validate_schema=validate_schema, json=login_data, params="verify_code=" + str(token))


def test_login_step2_wrong_verify_code():
    default_DB.default()
    create_new_user()
    Login_new_user()
    url = URL + "/users/verify_code_enable"
    client.patch(url, headers=get_current_user_header(), params="verify_code_enable=1")

    Login_new_user()
    with open(os.getcwd()+ '/Pytest/Default/User_data/verify_code.txt',
              'r', encoding="utf-8") as token_data:
        token = token_data.read()

    url = URL + "/auth/login/verify_code"
    request.post(url, 401, validate_response={'detail': '認證碼錯誤'}
                 , json=login_data, params="verify_code=" + str(int(token)+1))
