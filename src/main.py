from user.keeper import *
from user.creator import User


def sign_up(session_username, session_password):
    new_user = User(session_username, session_password)
    store(new_user)


def __check_entry(keyboard_entry: str):
    return True if keyboard_entry == 'y'.casefold() or keyboard_entry is None else False


def set_label(session_user, element_label, element_word):
    session_user.create_label(element_label, element_word)


username = str(input('username: '))
is_in_registry, _ = exists(username)
if not is_in_registry:
    print('User not found.')
    wants = str(input('Want to sign up? [Y/n] '))

    if wants == 'n'.casefold():
        exit()
    else:
        print('Write a password.')
        password = str(input())
        sign_up(username, password)
        user = User(username, password)
        store(user)
        print('Signed up!')
        exit(0)
else:
    password = str(input('password: '))
    user = User(username, password)
    if password_matches(user, password):
        print('Signed in!')
    else:
        print('Wrong password. ')
        response: int = 0
        while response != -1:
            wants = str(input('Want to try again? [Y/n] '))
            response = -1 if not __check_entry(wants) else print('Write a password. ')
            tryout = str(input())
            if password_matches(user, tryout):
                break
        if response == -1:
            exit(0)

    print('What do you want to do? ')
    opt: int = 2
    while opt != -1:
        print('0: view labels ')
        print('1: create new label ')
        print('-1: end execution ')
        opt: int = int(input())
        if opt == 0:
            print(deserialize_labels(user.name))
        elif opt == 1:
            label: str = input('Write the label for a new password. ')
            word: str = input('Write the password to be stored. ')
            set_label(user, label, word)
            update(user)
        elif opt == -1:
            exit(0)
        else:
            print('Wrong command. ')
