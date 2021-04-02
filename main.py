import re
from enum import Enum


class SignUpAction(Enum):
    LOGGED = 1
    REGISTER = 2


def check_username(username):
    if len(username) <= 3:
        print('The username is too short, please create a new username.')
        return False
    if len(username) >= 9:
        print('The username is too long, please create a new username.')
        return False
    return True


def ask_username():
    while True:
        username = input('Enter a username: ')
        if check_username(username):
            return username


def check_email(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if re.search(regex, email):
        return True
    print('Please enter a valid email: ')
    return False


def ask_email():
    while True:
        email = input('Enter an email: ')
        if check_email(email):
            return email


def check_password(password):
    if len(password) < 6:
        print('The password is too short.')
        return False
    upper_case = "[A-Z]"
    if re.search(upper_case, password) is None:
        print('The password does not containt uppercase.')
        return False
    lower_case = "[a-z]"
    if re.search(lower_case, password) is None:
        print('The password does not contain lowercase.')
        return False
    symbols = "[!#$%&'()@*+,-./\^_`{|}~]"
    if re.search(symbols, password) is None:
        print('The password does not containt special symbols.')
        return False
    return True


def ask_password():
    while True:
        password = input('Create a password: ')
        if check_password(password):
            return password


def check_match(password_confirmation):
    if password != password_confirmation:
        print('The passwords do not match.')
        return False
    print('You have sucessfully registered.')
    return True


def ask_confirmation():
    while True:
        password_confirmation = input('Please enter the password again: ')
        if check_match(password_confirmation):
            return password_confirmation


def login_find(username_log, password_log):
    try:
        with open('data.txt', 'r') as file:
            data = file.read().split('\n')

            for x in data:
                print(x)
                p = x.split(", ")
                if len(p) >= 2:
                    if p[0] == username_log and p[1] == password_log:
                        print('You have sucessfully logged in as ' + username_log)
                        return True
            print('The username or password are incorrect.')
            return False
    except Exception as e:
        print(e)
        return False


def ask_login_or_register():
    while True:
        choice = input('If u already have an account and you want to login - type "login", if you want to sign up - type "register": ')
        if choice == 'login':
            username_log = input('Please enter an username: ')
            password_log = input('Please enter a password: ')
            if login_find(username_log, password_log):
                return SignUpAction.LOGGED
            continue
        if choice == 'register':
            return SignUpAction.REGISTER
        print('You can only input "login" or "register".')


def write_down(username, email, password):
    with open('data.txt', 'a') as f:
        f.write('{}, {}, {}\n'.format(username, password, email))


result = ask_login_or_register()
if result == SignUpAction.REGISTER:
    username = ask_username()
    email = ask_email()
    password = ask_password()
    password_confirmation = ask_confirmation()
    write_down(username, email, password)
print('Done')
