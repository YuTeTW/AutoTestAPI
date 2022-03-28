from Pytest.Default import default_DB
from ..request import Request
from ..user_login import *
import json, os

request = Request()
url = URL + "/fasteyes_device/{fasteyes_uuid}"