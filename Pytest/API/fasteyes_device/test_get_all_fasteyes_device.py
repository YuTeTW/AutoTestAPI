from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
url = URL + "/fasteyes_device/all"

def test_get_all_fasteyes_device_RD():
    default_DB.default()
    Login_RD()
    request.get(url, 200, headers=get_current_user_header())

def test_get_all_fasteyes_device_fail_admin():
    default_DB.default()
    Login_admin()
    request.get(url, 401, validate_response={'detail': '權限不夠'}, headers=get_current_user_header())

def test_get_all_fasteyes_device_fail_HR():
    default_DB.default()
    Login_HR()
    request.get(url, 401, validate_response={'detail': '權限不夠'}, headers=get_current_user_header())

def test_get_all_fasteyes_device_fail_normal_user():
    default_DB.default()
    Login_normal_user()
    request.get(url, 401, validate_response={'detail': '權限不夠'}, headers=get_current_user_header())
