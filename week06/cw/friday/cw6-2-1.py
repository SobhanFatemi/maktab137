class User:
    users = []
    def __init__(self, user):
        self.user = user
        self.users.append(self.user)

    @classmethod
    def get_user_count(cls):
        return len(cls.users)

u1 = User("Alice")
u2 = User("Bob")

print(User.get_user_count())