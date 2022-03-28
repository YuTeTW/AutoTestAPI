from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
url = URL + "/auth/pingServer"
with open(os.getcwd() + "/Pytest/API/user/validate_schema/user_model.json"
        , encoding="utf-8") as json_file:
    validate_schema = json.load(json_file)

def test_test_pingserver_success():
    default_DB.default()
    Login_admin()
    request.post(url, 200, validate_schema=validate_schema, headers=get_current_user_header())
