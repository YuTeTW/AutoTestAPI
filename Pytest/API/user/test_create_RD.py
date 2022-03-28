from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
url = URL + "/users/RD"

def data(name, email, group):
    return {
        "name": name,
        "password": "1234",
        "email": email,
        "info": {
            "address": "台北市中山區民權東路一段"
        },
        "group": {
            "name": group
        }
    }

with open(os.getcwd() + "/Pytest/API/user/validate_schema/user_model.json"
        , encoding="utf-8") as json_file:
    validate_schema = json.load(json_file)

def test_create_Admin_success():
    default_DB.default()
    request.post(url, 200, validate_schema=validate_schema,
                 json=data(name="example_RD",
                           email="example_RD@fastwise.net",
                           group="example_RD_group"))


def test_cteate_Admin_fail_of_Email_already_registered():
    default_DB.default()
    request.post(url, 400, validate_response={"detail": "Email already registered"},
                 json=data(name="example_RD",
                           email="Test_RD@fastwise.net",
                           group="example_RD"))


def test_cteate_Admin_fail_of_Name_already_registered():
    default_DB.default()
    request.post(url, 400, validate_response={"detail": "Name already exist"},
                 json=data(name="Test_RD",
                           email="example_RD@fastwise.net",
                           group="example_RD"))


def test_cteate_Admin_fail_of_Group_name_already_exist():
    default_DB.default()
    request.post(url, 400, validate_response={"detail": "Group name already exist"},
                 json=data(name="example_RD",
                           email="example_RD@fastwise.net",
                           group="Test_RD_Group"))





