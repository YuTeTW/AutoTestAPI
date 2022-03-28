import json
from Pytest import *

def get_current_user_header():
    with open(json_data_path + 'API/user/create_user/Headers.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return {"Authorization": "Bearer " + data["access_token"]}

def Login_RD():
    url = URL + "/auth/login"
    login_data = {
        "email": "Test_RD@fastwise.net",
        "password": "test"
    }
    response = client.post(url, json=login_data)
    with open(json_data_path + 'API/user/create_user/Headers.json', 'w', encoding='utf-8') as outfile:
        json.dump(response.json(), outfile)

def Login_admin():
    url = URL + "/auth/login"
    login_data = {
        "email": "Test_Admin@fastwise.net",
        "password": "test"
    }
    response = client.post(url, json=login_data)
    with open(json_data_path + 'API/user/create_user/Headers.json', 'w', encoding='utf-8') as outfile:
        json.dump(response.json(), outfile)


def Login_HR():
    url = URL + "/auth/login"
    login_data = {
        "email": "Test_HR@fastwise.net",
        "password": "test"
    }
    response = client.post(url, json=login_data)
    with open(json_data_path + 'API/user/create_user/Headers.json', 'w', encoding='utf-8') as outfile:
        json.dump(response.json(), outfile)


def Login_normal_user():
    url = URL + "/auth/login"
    login_data = {
        "email": "Test_normal_user@fastwise.net",
        "password": "test"
    }
    response = client.post(url, json=login_data)
    with open(json_data_path + 'API/user/create_user/Headers.json', 'w', encoding='utf-8') as outfile:
        json.dump(response.json(), outfile)

def create_new_user():
    url = URL + "/users/admin"
    user_data = {
      "name": "Dave",
      "password": "dave",
      "email": "judhaha@gmail.com",
      "info": {
        "address": "台北市中山區民權東路一段"
      },
      "group": {
        "name": "Test_Dave_Group"
      }
    }
    client.post(url, json=user_data)

def Login_new_user():
    url = URL + "/auth/login"
    login_data = {
        "email": "judhaha@gmail.com",
        "password": "dave"
    }
    response = client.post(url, json=login_data)
    with open(json_data_path + 'API/user/create_user/Headers.json', 'w', encoding='utf-8') as outfile:
        json.dump(response.json(), outfile)


