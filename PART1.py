# class UserManager():
#     def __init__(self, user):
#         self.user = user
#
#     def change_user_name(self, new_name):
#         self.user.name = new_name
#
#     def save_user(self):
#         file = open("users.txt", "a")
#         file.write(self.user)
#         file.close()


# SOLID вариант
class User():
    def __init__(self, name):
        self.name = name


class UserNameChanger():
    def __init__(self, user):
        self.user = user

    def change_name(self, new_name):
        self.user.name = new_name


class Saveuser():
    def __init__(self, user):
        self.user = user

    def save(self):
        file = open("users.txt", "a")
        file.write(self.user.name)
        file.close()


