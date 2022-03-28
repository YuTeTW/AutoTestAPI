from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
url = URL + "/users/setting"

user_info = {
  "email_alert": True,
  "language": 3
}

with open(os.getcwd() + "/Pytest/API/user/validate_schema/user_model.json"
        , encoding="utf-8") as json_file:
    validate_schema = json.load(json_file)

def test_patch_users_setting():
    default_DB.default()
    Login_normal_user()
    request.patch(url, 200, validate_schema=validate_schema
                  , json=user_info,headers=get_current_user_header())
