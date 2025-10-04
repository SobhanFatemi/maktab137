def join_user (first_user: tuple, second_user : tuple, is_admin = True):
    """
    It joins two users

    Args: 
    first_user: tuple the first user

    Return:
    it counts all users
    """
    return f"{first_user[1]}, {second_user[1]}"

from user_handler import print_users as show_users
from data_handler import get_user_data

user_data = get_user_data()
show_users(user_data)

result: str = join_user(user_data[1], user_data[0])

print(result)

numbers: dict = {
    'item1': 3,
    'item2': 45,
    'item3': True,
    'item4': {'name': 'Hello'},
    'item5': [1, 3, 'yes']
}

print(numbers['item5'])

# doc in the function
print(join_user.__doc__)