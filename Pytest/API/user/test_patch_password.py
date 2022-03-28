from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
url = URL + "/users/password"

with open(os.getcwd() + "/Pytest/API/user/validate_schema/user_model.json"
        , encoding="utf-8") as json_file:
    validate_schema = json.load(json_file)

def password(old_password):
    return {
      "new_password": "test_2",
      "old_password": old_password
    }

def test_patch_password_successful():
    default_DB.default()
    Login_HR()
    request.patch(url, 200, validate_schema=validate_schema, json=password("test"),
          headers=get_current_user_header())


def test_patch_password_fail():
    default_DB.default()
    request.patch(url, 401, validate_schema={'detail': '舊密碼錯誤'},
          json=password("test_3"),
          headers=get_current_user_header())
