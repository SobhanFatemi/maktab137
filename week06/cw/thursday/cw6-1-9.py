class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def info(self):
        print(f"Username: {self.username} Email: {self.email}")

    def login(self):
        print(f"{self.username} has logged in.")

class AdminUser(User):
    def __init__(self, username, email, privileges):
        super().__init__(username, email)
        self.privileges = privileges
    
    def ban_user(self, user):
        print(f"{self.username} has banned user {user}")

    def show_privileges(self):
        print(f"Your privileges are: {self.privileges}")

class NormalUser(User):
    def __init__(self, username, email, comments):
        super().__init__(username, email)
        self.comments = comments

    def post_comments(self, text):
        self.comments.append(text)
        print(f"{self.username} posted a new comment: '{text}'")

    def show_comments(self):
        print(f"All the comments include: {self.comments}")

admin1 = AdminUser("NimaOstad", "nimaostad55@gmail.com", ["delete", "ban_users", "posts", "edit_settings"])
admin1.ban_user("SobhanFatemi")
admin1.show_privileges()

sara = NormalUser("SaraRahmati", "sararahmati55@gmail.com", [])
sara.post_comments("I liked this video!")
sara.post_comments("I didn't like this video!")
sara.show_comments()

ali = NormalUser("AliAlavi", "alialavi55@gmail.com", [])
ali.post_comments("I liked this video!")
ali.post_comments("I didn't like this video!")
ali.show_comments()

users = [admin1, ali, sara]

for user in users:
    user.login()
    user.info()