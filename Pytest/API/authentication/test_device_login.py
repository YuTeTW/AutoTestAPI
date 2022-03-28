from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
url = URL + "/auth/device-login"

with open(os.getcwd() + "/Pytest/API/validate_staff_schema.json"
        , encoding="utf-8") as json_file:
    validate_schema = json.load(json_file)

def test_device_login_RD():
    default_DB.default()
    login_data = {
        "email": "Test_RD@fastwise.net",
        "password": "test"
    }
    request.post(url, 200, validate_schema=validate_schema, json=login_data)

def test_device_login_Admin():
    default_DB.default()
    login_data = {
        "email": "Test_Admin@fastwise.net",
        "password": "test"
    }
    request.post(url, 200, validate_schema=validate_schema, json=login_data)

def test_device_login_HR():
    default_DB.default()
    login_data = {
        "email": "Test_HR@fastwise.net",
        "password": "test"
    }
    request.post(url, 200, validate_schema=validate_schema, json=login_data)

def test_device_login_normal_user():
    default_DB.default()
    login_data = {
        "email": "Test_normal_user@fastwise.net",
        "password": "test"
    }
    request.post(url, 200, validate_schema=validate_schema, json=login_data)

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