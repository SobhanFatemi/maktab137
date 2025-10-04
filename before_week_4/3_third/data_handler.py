# SOC
# () Can't be changed (use capital letter for things that you don't want changed)\
USERS: tuple = ((1, "Sobhan Fatemi", "M", 23), (2, "Fateme Keshvari", "F", 19),
                (3, "Arman Fatemi", "M", 15), (4, "Amir Shahrokh", "M", 23))


def get_user_data():
    return USERS

# uses key value
def user_get_dict_data():
    users: dict = {}

    user_list = get_user_data()
    for user in user_list:
        users[user[0]]