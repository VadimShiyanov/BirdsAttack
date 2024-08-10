import requests
import hashlib
import json
import os

SERVER_URL = "https://localhost:8000"

def register(username, password):
    phash = hashlib.sha256(password.encode()).hexdigest()
    answer = json.loads(requests.get(SERVER_URL + f"/reg/{username};{phash}", verify=False).text)
    if answer["success"] == True:
        with open("sid.gfile", 'w') as gfile:
            gfile.write(username + ":" + answer["text"])
        return True
    else:
        return False

def login(username, password):
    phash = hashlib.sha256(password.encode()).hexdigest()
    answer = json.loads(requests.get(SERVER_URL + f"/login/{username};{phash}", verify=False).text)
    if answer["success"] == True:
        with open("sid.gfile", 'w') as gfile:
            gfile.write(username + ":" + answer["text"])
        return True
    else:
        return False

def send_score(score: int):
    if not os.path.exists("sid.gfile"):
        raise Exception("Для начала необходимо выполнить backend.login или backend.register")
    else:
        with open("sid.gfile", "r") as gfile:
            data = gfile.read()
        data = data.replace("\n", '')
        username, sid = data.split(":")
        answer = json.loads(requests.get(SERVER_URL + f"/update_score/{username};{sid};{str(score)}", verify=False).text)
        if answer["success"] == True:
            return True
        else:
            return False

def get_my_score():
    if not os.path.exists("sid.gfile"):
        raise Exception("Для начала необходимо выполнить backend.login или backend.register")
    else:
        with open("sid.gfile", "r") as gfile:
            data = gfile.read()
        data = data.replace("\n", '')
        username, sid = data.split(":")
        data = json.loads(requests.get(SERVER_URL + "/scores", verify=False).text)
        return str(data[username])

def get_my_username():
    if not os.path.exists("sid.gfile"):
        raise Exception("Для начала необходимо выполнить backend.login или backend.register")
    else:
        with open("sid.gfile", "r") as gfile:
            data = gfile.read()
        data = data.replace("\n", '')
        username, sid = data.split(":")
        return username

def all_scores():
    return json.loads(requests.get(SERVER_URL + "/scores", verify=False).text)

def onetime_connection_check():
    try:
        response = requests.get(SERVER_URL, verify=False, timeout=5)
        if response.ok:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        return False
