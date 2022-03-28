import json
from Pytest import *


def get_current_user_header():
    with open(json_data_path + 'Default/User_data/Headers.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return {"Authorization": "Bearer " + data["access_token"]}

def get_user_data(user):
    with open(json_data_path + 'Default/User_data/' + user + '.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

def get_uuid_data(uuid):
    with open(json_data_path + 'Default/UUID_data/' + uuid + '.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


################### default ####################
def clear_all_data_no_auth():
    url = URL + '/auth/clear_all_data_no_auth'
    client.delete(url)

def add_RD():
    url = URL + "/users/RD"
    RD_data = get_user_data("RD")
    client.post(url, json=RD_data)

def add_AdminUser():
    url = URL + "/users/admin"
    adminusers_data = get_user_data("Admin")
    client.post(url, json=adminusers_data)

def Login_RD():
    url = URL + "/auth/login"
    login_data = {
        "email": "Test_RD@fastwise.net",
        "password": "test"
    }
    response = client.post(url, json=login_data)
    with open(json_data_path + 'Default/User_data/Headers.json', 'w', encoding='utf-8') as outfile:
        json.dump(response.json(), outfile)

def create_Fasteyes_UUID():
    url = URL + "/fasteyes_uuid"
    para = {
        "creator": "Test",
        "product_number": "00"
    }
    response = client.post(url, json=para, headers=get_current_user_header())
    with open(json_data_path + 'Default/UUID_data/deviceuuid.json', 'w', encoding='utf-8') as outfile:
        json.dump(response.json(), outfile)

def refresh_1_Fasteyes_device():
    url = URL + "/fasteyes_uuid"
    with open(json_data_path + 'Default/UUID_data/deviceuuid.json', encoding='utf-8') as json_file:
        device_response = json.load(json_file)
    device_uuid = device_response["uuid"]
    uuid_data = {
        "hardware_uuid": "b3a99284-02f7-4b7d-8e08-85b5e3081501",
        "device_uuid": str(device_uuid)
    }
    response = client.patch(url, json=uuid_data, headers=get_current_user_header())
    with open(json_data_path + 'Default/UUID_data/deviceuuid2.json', 'w', encoding='utf-8') as outfile:
        json.dump(response.json(), outfile)
    assert response.status_code == 200


def regist_device():
    url = URL + "/fasteyes_device"
    with open(json_data_path + 'Default/UUID_data/deviceuuid2.json', encoding='utf-8') as json_file:
        device_data = json.load(json_file)
    device_uuid = device_data["uuid"]
    device_data = {
        "name": "Dave",
        "description": "string",
        "device_uuid": device_uuid
    }

    response = client.post(url, json=device_data, headers=get_current_user_header())
    with open(json_data_path + 'Default/UUID_data/deviceuuid3.json', 'w', encoding='utf-8') as outfile:
        json.dump(response.json(), outfile)
    assert response.status_code == 200

def Login_admin():
    url = URL + "/auth/login"
    login_data = {
        "email": "Test_Admin@fastwise.net",
        "password": "test"
    }
    response = client.post(url, json=login_data)
    with open(json_data_path + 'Default/User_data/Headers.json', 'w', encoding='utf-8') as outfile:
        json.dump(response.json(), outfile)

def invite_HR_user():
    url = URL + "/users/invite"
    HR_data = {
        "email": "Test_HR@fastwise.net",
        "level": 3
    }
    client.post(url, json=HR_data, headers=get_current_user_header())


def create_HR_user():
    with open(os.getcwd()+ '/Pytest/Default/User_data/invite_token.txt', 'r', encoding="utf-8") as token_data:
        token = token_data.read()
    url = URL + "/users/create/" + str(token)
    HR_data = get_user_data("HR")
    response = client.post(url, json=HR_data, headers=get_current_user_header())
    assert response.status_code == 200


def invite_noarmal_user():
    url = URL + "/users/invite"
    HR_data = {
        "email": "Test_normal_user@fastwise.net",
        "level": 4
    }
    client.post(url, json=HR_data, headers=get_current_user_header())


def create_normal_user():
    with open(os.getcwd()+ '/Pytest/Default/User_data/invite_token.txt', 'r', encoding="utf-8") as token_data:
        token = token_data.read()
    url = URL + "/users/create/" + str(token)
    HR_data = get_user_data("normal_user")
    client.post(url, json=HR_data, headers=get_current_user_header())


def create_department():
    url = URL + "/department"
    department_data = {
        "name": "Test_job"
    }
    client.post(url, json=department_data, headers=get_current_user_header())


def create_staff():
    url = URL + "/staffs"
    with open(json_data_path + 'Default/staff_data/staff.json', encoding='utf-8') as json_file:
        staff_data = json.load(json_file)
    client.post(url, json=staff_data, headers=get_current_user_header())


def StaffFaceImages():
    url = URL + "/staffs/1/faces"
    files = {'Image_file': open(json_data_path + 'Default/staff_data/Dave.jpg', 'rb')}
    response = client.post(url, files=files, headers=get_current_user_header())
    assert response.status_code == 200


def StaffFaceFeature():
    url = URL + "/staffs/1/raw_face_features"
    with open(json_data_path + 'Default/staff_data/feature.txt', 'rb') as feature:
        raw_face_feature = feature.read()
    face_data = {
        "feature": raw_face_feature
    }
    response = client.post(url, params=face_data, headers=get_current_user_header())
    assert response.status_code == 200


###############################################
def default():
    clear_all_data_no_auth()
    add_RD()
    add_AdminUser()
    Login_RD()
    create_Fasteyes_UUID()
    refresh_1_Fasteyes_device()
    regist_device()
    Login_admin()
    invite_HR_user()
    create_HR_user()
    invite_noarmal_user()
    create_normal_user()
    create_department()
    create_staff()
    StaffFaceImages()
    StaffFaceFeature()











