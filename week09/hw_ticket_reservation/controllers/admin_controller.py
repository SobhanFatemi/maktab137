<<<<<<< HEAD
from models.user import UserModel


class AdminController:
    def __init__(self):
        self.service = UserModel()

    def make_admin(self):
        try:
            uid = int(input("User ID to promote: "))
        except ValueError:
            print("Invalid number!")
            return

        self.service.promote(uid)

=======
from models.user import UserModel


class AdminController:
    def __init__(self):
        self.service = UserModel()

    def make_admin(self):
        try:
            uid = int(input("User ID to promote: "))
        except ValueError:
            print("Invalid number!")
            return

        self.service.promote(uid)

>>>>>>> 0733a7809c589505f0dd4b70e2c17c2f627c496b
    