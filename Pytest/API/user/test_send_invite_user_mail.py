from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os, random

request = Request()

url = URL + "/users/invite"
def invite_data(email="example@fastwise.net", level=random.randrange(2,5)):
    return {
        "email": email,
        "level": level
    }

def test_invite_email_success_RD():
    default_DB.default()
    Login_RD()
    request.post(url, 200,
                 validate_response="Email has sended"
                 , json=invite_data(), headers=get_current_user_header())


def test_invite_email_success_admin():
    default_DB.default()
    Login_admin()
    request.post(url, 200,
                 validate_response="Email has sended"
                 , json=invite_data(), headers=get_current_user_header())


def test_invite_email_success_HR():
    default_DB.default()
    Login_HR()
    request.post(url, 200,
                 validate_response="Email has sended"
                 , json=invite_data(), headers=get_current_user_header())


def test_invite_email_success_normal_user():
    default_DB.default()
    Login_normal_user()
    request.post(url, 200,
                 validate_response="Email has sended"
                 , json=invite_data(), headers=get_current_user_header())


def test_send_email_fail_about_email_already_registered():
    default_DB.default()
    Login_admin()
    request.post(url, 400, validate_response={'detail': 'Email already registered'},
            json=invite_data("Test_HR@fastwise.net", 3),
            headers=get_current_user_header())


def test_send_email_fail_about_level_error():
    default_DB.default()
    Login_admin()
    request.post(url, 400, validate_response={'detail': '權限 level 請輸入 2~4'}
,
            json=invite_data(level=5),
            headers=get_current_user_header())






