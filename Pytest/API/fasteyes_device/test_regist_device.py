# from Pytest.Default import default_DB
# from ..request import Request
# from ..user_login import *
# import json, os
# import uuid
#
# request = Request()
# url = URL + "/fasteyes_device"
#
# device_data = {
#     "name": "test_new_device",
#     "description": "string",
#     "device_uuid": str(uuid.UUID)
# }
#
# def test_regist_device():
#     # default_DB.default()
#     Login_admin()
#     request.post(url, 200, json=device_data, headers=get_current_user_header())