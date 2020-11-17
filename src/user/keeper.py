from user.creator import User
from src.path.editor import Editor
import bcrypt

log = Editor.edit_given_path('resources/auth.txt').replace('user/', '')


def store(session_user: User):
    is_in_registry, _ = exists(session_user.name)
    if is_in_registry:
        return
    with open(log, 'a') as users:
        elements = '{}'.format(session_user.elements).replace('{', '').replace('}', '')
        users.write('username: {}\n'
                    'password: {}\n'
                    'elements: {}\n'
                    '\n'
                    .format(session_user.name, session_user.password, elements))


def exists(username: str) -> bool and int:
    """Checks the lines from the users registry, one by one.
    To say that one user is already in the registry, we
    need to ensure that it's username was already written in the file.

    Checks the beginning of each line as
        <name>: ...
    :param username: to be checked.
    :return: a boolean flag stating if the given user is already
             signed up in the system.
    """
    # log = __get_path_for(username)
    with open(log, 'r') as users:
        lines = users.readlines()
        for i in range(len(lines)):
            line = lines[4*i]
            _, name = line.split()
            if name == username:
                return True, 4*i
            if 4*(i + 1) + 1 > len(lines):
                break
    return False, 0


def password_matches(session_user: User, password: str):
    if session_user.password == bcrypt.hashpw(password.encode('UTF-8'), session_user.password):
        return True
    return False


def deserialize_labels(username: str):
    if not exists(username):
        return []
    with open(log, 'r') as users:
        _, username_line = exists(username)
        return users.readlines()[username_line + 2]


def update(session_user: User):
    if not exists(session_user.name):
        return
    users = open(log, 'r')
    lines = users.readlines()
    _, username_line = exists(session_user.name)
    users.close()

    with open(log, 'w') as users:
        elements_line = username_line + 2
        new_elements = '{}'.format(session_user.elements).replace('{', '').replace('}', '')
        lines[elements_line] = 'elements: ' + '{' + new_elements + '}\n'
        users.writelines(lines)
