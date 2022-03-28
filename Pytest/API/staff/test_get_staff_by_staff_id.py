from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
def url(staff_id):
    return URL + "/staffs/" + str(staff_id)

def test_get_staff_by_id():
    default_DB.default()
    Login_admin()
    request.get(url(1), 200, headers=get_current_user_header())

def test_get_staff_wrong_level():
    default_DB.default()
    Login_normal_user()
    request.get(url(1), 401, validate_response={'detail': '權限不夠'},
                headers=get_current_user_header())

def test_staff_is_not_exist():
    default_DB.default()
    Login_admin()
    request.get(url(9999), 404, validate_response={'detail': 'staff is not exist'},
                headers=get_current_user_header())

def test_staff_is_not_in_this_group():
    default_DB.default()
    Login_RD()
    request.get(url(1), 401, validate_response={'detail': "staff id不在登入的使用者的group"},
                headers=get_current_user_header())


