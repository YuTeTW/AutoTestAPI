from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
url = URL + "/users"

with open(os.getcwd() + "/Pytest/API/user/validate_schema/user_model.json"
        , encoding="utf-8") as json_file:
    validate_schema = json.load(json_file)

def test_get_all_user_RD():
    default_DB.default()
    Login_RD()
    request.get(url, 200, validate_schema=validate_schema, headers=get_current_user_header())

def test_get_all_user_admin():
    default_DB.default()
    Login_admin()
    request.get(url, 200, validate_schema=validate_schema, headers=get_current_user_header())

def test_get_all_user_HR():
    default_DB.default()
    Login_HR()
    request.get(url, 401, validate_response={'detail': '權限不夠'}, headers=get_current_user_header())

def test_get_all_user_normal_user():
    default_DB.default()
    Login_normal_user()
    request.get(url, 401, validate_response={'detail': '權限不夠'}, headers=get_current_user_header())
