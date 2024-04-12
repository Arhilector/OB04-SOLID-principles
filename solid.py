class UserManager():
    def __init__(self, user):
        self.user = user

    def change_user_name(self, new_name):
        self.user.name = new_name
        