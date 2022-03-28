from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
url = URL + "/auth/forget_password"

def test_send_Send_Forget_Password_Email():
    default_DB.default()
    create_user()
    request.post(url, 200, validate_response="SendForgetPasswordEmail Done"
                 , params={"email" : "dave@fastwise.net"})

def test_send_Send_Forget_Password_Email_fail():
    default_DB.default()
    request.post(url, 404, validate_response={'detail': 'Email does not exist'}
                 , params={"email" : "example@fastwise.net"})

