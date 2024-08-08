import requests
import hashlib
import json
import os

SERVER_URL = "http://localhost:8000"

def register(username, password):
    phash = hashlib.sha256(password.encode()).hexdigest()
    answer = json.loads(requests.get(SERVER_URL + f"/reg/{username};{phash}").text)
    if answer["success"] == True:
        with open("sid.gfile", 'w') as gfile:
            gfile.write(username + ":" + answer["text"])
        return True
    else:
        return False

def login(username, password):
    phash = hashlib.sha256(password.encode()).hexdigest()
    answer = json.loads(requests.get(SERVER_URL + f"/login/{username};{phash}").text)
    if answer["success"] == True:
        with open("sid.gfile", 'w') as gfile:
            gfile.write(username + ":" + answer["text"])
        return True
    else:
        return False

def update_score():
    if not os.path.exists("sid.gfile"):
        raise Exception("Для начала необходимо выполнить backend.login или backend.register")
    else:
        with open("sid.gfile", "r") as gfile:
            data = gfile.read()
        data = data.replace("\n", '')
        username, sid = data.split(":")
        answer = json.loads(requests.get(SERVER_URL + f"/update_score/{username};{sid}").text)
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
        data = json.loads(requests.get(SERVER_URL + "/scores").text)
        return str(data[username])

def all_scores():
    return json.loads(requests.get(SERVER_URL + "/scores").text)