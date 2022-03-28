from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
url = URL + "/staffs"

def staff_data(department_id, serial_number):
    return {
      "department_id": department_id,
      "serial_number": serial_number,
      "info": {
        "name": "Test_staff_2",
        "card_number": "1212221",
        "email": "test_staff@fastwise.net",
        "gender": 2,
        "national_id_number": "string",
        "birthday": "1993-01-01T00:00",
        "telephone_number": "0987654321"
      },
      "start_date": "2002-12-25T00:00",
      "status": "1"
    }

def test_create_staff():
    default_DB.default()
    Login_admin()
    request.post(url, 200, json=staff_data(department_id=1, serial_number=2),
                 headers=get_current_user_header())

def test_Serveral_number_already_exist():
    default_DB.default()
    Login_admin()
    request.post(url, 400, validate_response= {'detail': 'Serveral_number already exist in this group'},
                 json=staff_data(department_id=1, serial_number=10000000000),
                 headers=get_current_user_header())

def test_department_id_is_not_exist():
    default_DB.default()
    Login_admin()
    request.post(url, 400, validate_response= {'detail': 'department id is not exist'},
                 json=staff_data(department_id=2, serial_number=2),
                 headers=get_current_user_header())


