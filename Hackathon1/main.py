import faker
from login import Login


def main():
    active_user = Login().login()
    print(active_user)
# class User:
#     user_list = []
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
#
#     @classmethod
#     def create_fake_users(cls,amount):
#         for i in range(amount):
#             username =
#             user = User()
main()