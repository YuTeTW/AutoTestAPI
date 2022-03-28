from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
files = {'Image_file': open(json_data_path + 'Default/staff_data/Dave.jpg', 'rb')}


def url(staff_id):
    return URL + "/staffs/" + str(staff_id) + "/faces"


def test_get_staff_face_file():
    default_DB.default()
    Login_admin()
    request.post(url(1), 200, files=files,
                 headers=get_current_user_header())

def test_uploda_staff_face_wrong_level():
    default_DB.default()
    Login_normal_user()
    request.post(url(1), 401, files=files, validate_response={"detail": "權限不夠"},
                headers=get_current_user_header())


def test_staff_is_not_exist():
    default_DB.default()
    Login_RD()
    request.post(url(9 ** 9), 404, files=files, validate_response={'detail': 'staff is not exist'},
                headers=get_current_user_header())


def test_staff_is_not_in_group():
    default_DB.default()
    Login_RD()
    request.post(url(1), 401, files=files, validate_response={'detail': 'staff id不在登入的使用者的group'},
                headers=get_current_user_header())

# 未完