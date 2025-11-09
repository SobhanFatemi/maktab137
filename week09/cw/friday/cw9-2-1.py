from dataclasses import dataclass, field
import hashlib
from datetime import datetime
import pickle

@dataclass
class User:
    name: str
    email: str
    password: str
    created_at: datetime

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password_hash = self.hash_pass(password)

    def hash_pass(self, password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()
    

class UserManager:
    def __init__(self, filename):
        self.filename = filename
        self.users = None

    def load_file(self):
        with open(self.filename) as file:
            self.users = pickle.load(file)

    def save_user(self):
        with open(self.filename) as file:
            pickle.dump(file, self.users)

    def add_user(self, name: str, email: str, password: str):
        user = User(name, email, password)
        self.users.append(user)
        self.save_user()

    def delete_user(self, email):
        for user in self.users:
            if user.email == email:
                del self.users(user)
                break

    def search_user(self, email):
        for user in self.users:
            if user.email == email:
                return user
        print("User not Found!")
        return None
    
    def show_users(self):
        if not self.users:
            print("There are now users to show!")
            return None
        for i, user in enumerate(self.users):
            print(f"{i+1}. {user.name}")
            
        




