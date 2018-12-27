from app.models import db
import hashlib


def send_token(username, password):
    password_hash = password
    print(password_hash)
    print(username)
    user = db.applicant.find_one({"$and": [{'user_name': username}, {'password_hash': password_hash}]})
    if not user:
        return False, "user doesn't exist"
    # if not user['is_valid']:
    #     return False, "user not valid"
    return True, username
