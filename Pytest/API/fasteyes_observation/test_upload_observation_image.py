from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
url = URL + "/Files/upload/image/device/{device_id}/file_name/{file_name}"