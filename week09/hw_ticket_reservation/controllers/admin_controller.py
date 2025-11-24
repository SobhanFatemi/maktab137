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

    