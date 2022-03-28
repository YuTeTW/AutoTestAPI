from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
url = URL + "/users/info"

with open(os.getcwd() + "/Pytest/API/user/validate_schema/user_model.json"
        , encoding="utf-8") as json_file:
    validate_schema = json.load(json_file)

def test_patch_user_info():
    default_DB.default()
    Login_HR()
    request.patch(url, 200, validate_schema=validate_schema ,json={"name": "test_name"}, headers=get_current_user_header())


def test_patch_user_info_fail():
    default_DB.default()
    Login_normal_user()
    request.patch(url, 400,
                  validate_response={'detail': "Name already exist in this group"},
                  json={"name": "Test_HR"},
                  headers=get_current_user_header())
