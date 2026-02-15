import json
import bcrypt

def load_users():
    with open("data/users.json", "r") as f:
        return json.load(f)

def save_users(users):
    with open("data/users.json", "w") as f:
        json.dump(users, f, indent=4)

def authenticate(username, password):
    users = load_users()
    if username not in users:
        return False

    hashed = users[username]["password"].encode()
    return bcrypt.checkpw(password.encode(), hashed)