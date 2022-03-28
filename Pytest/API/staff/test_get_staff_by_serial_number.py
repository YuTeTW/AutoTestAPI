from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
def url(serial_number):
    return URL + "/staffs/SerialNumber/" + str(serial_number)

with open(os.getcwd() + "/Pytest/API/staff/json_data/validate_staff_schema.json"
        , encoding="utf-8") as json_file:
    validate_schema = json.load(json_file)

def test_get_staff_by_serial_number_admin():
    default_DB.default()
    Login_admin()
    request.get(url(10000000000), 200, validate_schema=validate_schema,
                headers=get_current_user_header())

def test_get_staff_by_serial_number_HR():
    default_DB.default()
    Login_HR()
    request.get(url(10000000000), 200, validate_schema=validate_schema,
                headers=get_current_user_header())

def test_get_staff_wrong_level():
    default_DB.default()
    Login_normal_user()
    request.get(url(10000000000), 401, validate_response={'detail': '權限不夠'},
                headers=get_current_user_header())

def test_staff_is_not_exist():
    default_DB.default()
    Login_RD()
    request.get(url(10000000000), 404, validate_response={'detail': 'staff is not exist'},
                headers=get_current_user_header())