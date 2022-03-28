from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()

HR_data = {
    "email": "Test_normal_user_2@fastwise.net",
    "level": 4
}

normal_user_data = {
  "name": "Test_normal_user_2",
  "password": "test",
  "email": "Test_normal_user_2@fastwise.net",
  "info": {
    "address": "台北市中山區民權東路一段"
  }
}

with open(os.getcwd() + "/Pytest/API/user/validate_schema/user_model.json"
        , encoding="utf-8") as json_file:
    validate_schema = json.load(json_file)


def test_create_normal_user():
    default_DB.default()
    Login_admin()
    url = URL + "/users/invite"
    client.post(url, json=HR_data, headers=get_current_user_header())
    with open(json_data_path + '/Default/User_data/invite_token.txt', 'r', encoding="utf-8") as token_data :
        token = token_data.read()
    url = URL + "/users/create/" + str(token)
    request.post(url, 200, validate_schema=validate_schema, json=normal_user_data )
