import datetime

def print_users (user_name):
    """
    It shows all users

    Args: 
    first_user: tuple the first user

    Return:
    it counts all users
    """

    print(f"Report {datetime.datetime.now()}")

    print("id\tfull name\tsex\tage")
    
    for user in user_name:
        print(user[0], user[1], user[2], user[3] , sep="\t")