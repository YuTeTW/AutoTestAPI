from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()

def url(user_id):
    return URL + "/auth/users/" + str(user_id) + "/change"

with open(os.getcwd() + "/Pytest/API/user/validate_schema/user_model.json"
        , encoding="utf-8") as json_file:
    validate_schema = json.load(json_file)

def test_change_HR_level_to_normal_user_level_success():
    default_DB.default()
    Login_admin()
    request.patch(url(3), 200, validate_schema=validate_schema,
                  headers=get_current_user_header(), params={"level" : 4})

def test_change_normal_user_to_level_to_HR_level_success():
    default_DB.default()
    Login_admin()
    request.patch(url(4), 200, validate_schema=validate_schema,
                  headers=get_current_user_header(), params={"level" : 3})

def test_change_level_fail_HR():
    default_DB.default()
    Login_HR()
    request.patch(url(4), 401, validate_response={'detail': '權限不夠'},
                  headers=get_current_user_header(), params={"level" : 3})

def test_change_level_fail_normal_user():
    default_DB.default()
    Login_normal_user()
    request.patch(url(4), 401, validate_response={'detail': '權限不夠'},
                  headers=get_current_user_header(), params={"level" : 3})

def test_change_level_fail_not_in_group():
    default_DB.default()
    Login_RD()
    request.patch(url(4), 404, validate_schema={'detail': "user is not in this group"},
                  headers=get_current_user_header(), params={"level" : 3})

def test_change_level_fail_change_self():
    default_DB.default()
    Login_admin()
    request.patch(url(2), 400, validate_schema={'detail': "請別做智障事把自己降級，謝謝！"},
                  headers=get_current_user_header(), params={"level" : 3})