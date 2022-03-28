from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
url = URL + "/staffs/GetAllStaffs"
# validate_staff_schema.json少了end_date的validate
with open(os.getcwd() + "/Pytest/API/staff/json_data/validate_staff_schema.json"
        , encoding="utf-8") as json_file:
    validate_schema = json.load(json_file)

def test_get_all_staff():
    default_DB.default()
    Login_RD()
    request.get(url, 200, validate_schema=validate_schema, headers=get_current_user_header())

def test_get_all_staff_wrong_level_admin():
    default_DB.default()
    Login_admin()
    request.get(url, 401, validate_response={"detail" : "權限不夠"}, headers=get_current_user_header())

def test_get_all_staff_wrong_level_HR():
    default_DB.default()
    Login_HR()
    request.get(url, 401, validate_response={"detail": "權限不夠"}, headers=get_current_user_header())

def test_get_all_staff_wrong_level_normal_user():
    default_DB.default()
    Login_normal_user()
    request.get(url, 401, validate_response={"detail" : "權限不夠"}, headers=get_current_user_header())
