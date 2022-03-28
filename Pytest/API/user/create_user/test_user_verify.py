# from Pytest import URL
# from Pytest.API.request import Request
# from Pytest.Default import default_DB
# from ..user_login import *
#
# request = Request()
#
# HR_data = {
#     "email": "Test_normal_user_2@fastwise.net",
#     "level": 4
# }
#
# def test_users_is_invited_verify_success():
#     default_DB.default()
#     Login_admin()
#     url = URL + "/users/invite"
#     client.post(url, json=HR_data, headers=get_current_user_header())
#     with open(json_data_path + '/Default/User_data/invite_token.txt', 'r', encoding="utf-8") as token_data :
#         token = token_data.read()
#     url = URL + "/users/verify/" + str(token)
#     request.get(url, 200)