from models.user import UserModel


class UserService:

    def username_exists(self, username):
        return UserModel.find_by_username(username) is not None

    def create_passenger(self, username, password, first_name, last_name, phone, birth_date):
        return UserModel.create_passenger(username, password, first_name, last_name, phone, birth_date)

    def authenticate(self, username, password):
        user = UserModel.find_by_username(username)
        if not user:
            return None
        if UserModel.password_matches(password, user):
            return user
        return None

    def promote(self, uid):
        return UserModel.promote(uid)
