from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
def url(staff_id):
    return URL + "/staffs/" + str(staff_id)

staff_info = {
    "name": "new_name",
    "card_number": "2",
    "email": "ricky@gmail.com",
    "national_id_number": "11111111",
    "birthday": "2022-12-25T00:00",
    "department_id": "5",
    "telephone_number": "0987654321",
    "status": "1",
}

def test_patch_staff_info():
    default_DB.default()
    Login_admin()
    request.patch(url(1), 200, json=staff_info, headers=get_current_user_header())


def test_uploda_staff_face_wrong_level():
    default_DB.default()
    Login_normal_user()
    request.patch(url(1), 401, json=staff_info, validate_response={"detail": "權限不夠"},
                headers=get_current_user_header())


def test_staff_is_not_exist():
    default_DB.default()
    Login_RD()
    request.patch(url(9 ** 9), 404, json=staff_info, validate_response={'detail': 'staff is not exist'},
                headers=get_current_user_header())


def test_staff_is_not_in_group():
    default_DB.default()
    Login_RD()
    request.patch(url(1), 401, json=staff_info, validate_response={'detail': 'staff id不在登入的使用者的group'},
                headers=get_current_user_header())

