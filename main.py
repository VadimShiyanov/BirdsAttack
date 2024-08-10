from typing import Union
from jxdb import JsonDB
from fastapi import FastAPI
import os, json, random, uvicorn

CFG = json.loads(open("config.json", 'r').read())
DB_PATH = "data.jxdb"
DB_PASS = CFG["server_db_password"]

app = FastAPI()

def sort_dict(d):
    return dict(sorted(d.items(), key=lambda item: int(item[1]), reverse=True))

def is_user_exists(uname):
    db = JsonDB()
    db.open(DB_PATH, DB_PASS)
    if uname.replace('\n', '') in db.keys():
        return True
    else:
        return False

def enter_db_data(key, value):
    db = JsonDB()
    db.open(DB_PATH, DB_PASS)
    db.set(key, value)
    db.save(DB_PATH, DB_PASS)

def check_phash(uname, phash):
    db = JsonDB()
    db.open(DB_PATH, DB_PASS)
    if db.get(uname)["phash"] == phash:
        return True
    else:
        return False

def check_sid(uname, phash):
    db = JsonDB()
    db.open(DB_PATH, DB_PASS)
    if db.get(uname)["sid"] == phash:
        return True
    else:
        return False

def get_sid(username):
    db = JsonDB()
    db.open(DB_PATH, DB_PASS)
    return db.get(username)["sid"]

def update_score_b(username, score):
    score = int(score)
    db = JsonDB()
    db.open(DB_PATH, DB_PASS)
    data = db.get(username)
    score_now = int(data["score"])
    if score > score_now:
        data["score"] = score
        db.set(username, data)
    db.save(DB_PATH, DB_PASS)

def get_scores():
    scores = {}
    db = JsonDB()
    db.open(DB_PATH, DB_PASS)
    for uname in db.keys():
        score = str(db.get(uname)['score'])
        scores[uname] = score
    return sort_dict(scores)

if not os.path.exists('data.jxdb'):
    def init_db():
        db = JsonDB()
        db.save(DB_PATH, DB_PASS)
    init_db()

@app.get("/")
def read_root():
    return {"Powered by github.com/ohmiu"}

@app.get("/reg/{username};{phash}")
def register_new_user(username: str, phash: str):
    try:
        if is_user_exists(username):
            raise Exception("User already exists")
        sid = str(random.randint(100000, 1000000000))
        enter_db_data(username, {"score": 0, "phash": phash, "sid": sid})
        return {"success": True, "text": sid}
    except Exception as merr:
        return {"success": False, "text": str(merr)}

@app.get("/login/{username};{phash}")
def login(username: str, phash: str):
    try:
        if check_phash(username, phash):
            sid = get_sid(username)
            return {"success": True, "text": sid}
        else:
            raise Exception("Incorrect password")
    except Exception as merr:
        return {"success": False, "text": str(merr)}

@app.get("/update_score/{username};{sid};{score}")
def update_score(username: str, sid: str, score: str):
    try:
        if check_sid(username, sid):
            update_score_b(username, score)
            return {"success": True, "text": "Score operation ended successfully"}
        else:
            raise Exception("Incorrect SID")
    except Exception as merr:
        return {"success": False, "text": str(merr)}

@app.get("/scores")
def get_all_scores():
    return get_scores()

if __name__ == "__main__":
    uvicorn.run("main:app", host=CFG["server_ip"], port=CFG["server_port"], reload=True)
