from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
url = URL + "/users/admin/2"

def test_delect_Admin_user_success():
    default_DB.default()
    Login_RD()
    request.delete(url, 200, validate_response="delete Done", headers=get_current_user_header())

def test_delect_Admin_user_by_Admin():
    default_DB.default()
    Login_admin()
    request.delete(url, 401, validate_response={'detail': '權限不夠'}, headers=get_current_user_header())

def test_delect_Admin_user_by_HR():
    default_DB.default()
    Login_HR()
    request.delete(url, 401, validate_response={'detail': '權限不夠'}, headers=get_current_user_header())

def test_delect_Admin_user_by_normal_user():
    default_DB.default()
    Login_normal_user()
    request.delete(url, 401, validate_response={'detail': '權限不夠'}, headers=get_current_user_header())

def test_delect_Admin_user_not_Admin_user():
    default_DB.default()
    url = URL + "/users/admin/3"
    Login_RD()
    request.delete(url, 400, validate_response={'detail': '此user 不是 Admin user'}, headers=get_current_user_header())

# 原始碼有誤
# def test_delect_Admin_user_not_exist():
#     default_DB.default()
#     url = URL + "/users/admin/6"
#     Login_RD()
#     request.delete(url, 400, validate_response={'detail': 'user 不存在'}, headers=get_current_user_header())

