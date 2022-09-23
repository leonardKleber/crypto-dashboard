from db import insert_into_users, get_all_users_data


def create_user(name, password):
    insert_into_users(name, password)


def check_name_availability(name):
    all_users_data = get_all_users_data()
    for i in all_users_data:
        if i[1] == name:
            return False
    return True


def check_login_validity(name, password):
    all_users_data = get_all_users_data()
    for i in all_users_data:
        if i[1] == name and i[2] == password:
            return True 
    return False


def get_user_id(name):
    all_users_data = get_all_users_data()
    for i in all_users_data:
        if i[1] == name:
            return i[0]