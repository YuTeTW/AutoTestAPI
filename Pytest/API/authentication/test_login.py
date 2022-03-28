from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
url = URL + "/auth/login"

with open(os.getcwd() + "/Pytest/API/validate_staff_schema.json"
        , encoding="utf-8") as json_file:
    validate_schema = json.load(json_file)

def test_login_RD():
    default_DB.default()
    login_data = {
        "email": "Test_RD@fastwise.net",
        "password": "test"
    }
    request.post(url, 200, validate_schema=validate_schema, json=login_data)

def test_login_Admin():
    default_DB.default()
    login_data = {
        "email": "Test_Admin@fastwise.net",
        "password": "test"
    }
    request.post(url, 200, validate_schema=validate_schema, json=login_data)

def test_login_HR():
    default_DB.default()
    login_data = {
        "email": "Test_HR@fastwise.net",
        "password": "test"
    }
    request.post(url, 200, validate_schema=validate_schema, json=login_data)

def test_login_normal_user():
    default_DB.default()
    login_data = {
        "email": "Test_normal_user@fastwise.net",
        "password": "test"
    }
    request.post(url, 200, validate_schema=validate_schema, json=login_data)

def test_Login_step1():
    default_DB.default()
    Login_HR()
    url_2 = URL + "/users/verify_code_enable"
    client.patch(url_2, headers=get_current_user_header(), params="verify_code_enable=1")
    login_data = {
        "email": "Test_HR@fastwise.net",
        "password": "test"
    }
    request.post(url, 202, validate_response={'detail': 'Login step1 Done'}, json=login_data)

def test_login_fail():
    default_DB.default()
    login_data = {
        "email": "incorrect_email@fastwise.net",
        "password": "test"
    }
    request.post(url, 401, validate_response={'detail': 'Incorrect email'}, json=login_data)

def test_login_RD_fail():
    default_DB.default()
    login_data = {
        "email": "Test_RD@fastwise.net",
        "password": "failpassword"
    }
    request.post(url, 401, validate_response={'detail': "Incorrect password"}, json=login_data)

