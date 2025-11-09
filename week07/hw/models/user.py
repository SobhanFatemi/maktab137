import datetime
import os
from utils.hashing import hash_password, check_password
from utils.file_utils import load_json, save_json
from utils.id_counters import user_id, admin_id
from config import USERS_PATH


class UserModel:

    @staticmethod
    def load_all():
        return load_json(USERS_PATH)

    @staticmethod
    def save_all(data):
        save_json(USERS_PATH, data)

    @staticmethod
    def find_by_username(username):
        for u in load_json(USERS_PATH):
            if u.get("username") == username:
                return u
        return None

    @staticmethod
    def find_by_id(uid):
        for u in load_json(USERS_PATH):
            if u.get("id") == uid:
                return u
        return None

    @staticmethod
    def create_passenger(username, password, first_name, last_name, phone, birth_date):
        global user_id
        users = load_json(USERS_PATH)

        data = {
            "id": user_id,
            "role": "passenger",
            "username": username,
            "password_hash": hash_password(password),
            "first_name": first_name,
            "last_name": last_name,
            "ph_number": phone,
            "birth_date": birth_date,
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        users.append(data)
        save_json(USERS_PATH, users)
        user_id += 1
        return data

    @staticmethod
    def create_admin(username, password, first_name, last_name, phone, birth_date):
        global admin_id
        users = load_json(USERS_PATH)

        data = {
            "id": admin_id,
            "role": "admin",
            "username": username,
            "password_hash": hash_password(password),
            "first_name": first_name,
            "last_name": last_name,
            "ph_number": phone,
            "birth_date": birth_date,
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        users.append(data)
        save_json(USERS_PATH, users)
        admin_id += 1
        return data

    @staticmethod
    def password_matches(password, user_dict):
        return check_password(password, user_dict.get("password_hash", ""))

    @staticmethod
    def promote(uid):
        users = load_json(USERS_PATH)

        for u in users:
            if u.get("id") == uid:
                if u.get("role") == "admin":
                    print("User is already an admin!")
                    return False 

                make_sure = input(f"Are you sure you want to make '{u['username']}' admin? (y/n): ").lower()
                if make_sure != 'y':
                    print("Operation cancelled.")
                    return None  

                u["role"] = "admin"
                save_json(USERS_PATH, users)
                print(f"'{u['username']}' is now an admin!")
                return True

        print("User not found!")
        return False  