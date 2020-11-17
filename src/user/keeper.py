from user.creator import User
from src.path.editor import Editor
import bcrypt

log = Editor.edit_given_path('resources/auth.txt').replace('user/', '')


def store(session_user: User):
    """Checks if user exists in registry. If it does, it will not be stored
    (although it can be updated). It is needed to append ('a') a new user in the
    text file in order to not overwrite. Users are always stored as:
        0 * iterator -> username
        1 * iterator -> digested password
        2 * iterator -> elements and labels
        3 * iterator -> blank line
    :param session_user: to be stored inside 'resources/auth.txt'
    """
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
    """Checks the lines of the registry.
    To say that one user is already in it, we
    need to ensure that it's username is already written in the file.
    As every line that has a username is a multiple of four, we only check those.
    :param username: to be checked.
    :return: a boolean flag stating if the given user is already
             signed up in the system.
    """
    with open(log, 'r') as users:
        lines = users.readlines()
        for i in range(len(lines)):
            line = lines[4*i]  # Username lines.
            _, name = line.split()  # <username tag> and <username for comparison>
            if name == username:
                return True, 4*i
            if 4*(i + 1) + 1 > len(lines):  # Checks if another loop is possible to prevent a index out of range.
                break
    return False, 0


def password_matches(session_user: User, key_to_compare: str):
    """Gets a typed password for comparison, encoded,
    combines it with the one stored in the registry to generate a
    new digest and then compares the new digest with the one that
    is stored.
    :param session_user: to see if it's password matches the one typed.
    :param key_to_compare: typed during execution.
    :return:
    """
    if session_user.password == bcrypt.hashpw(key_to_compare.encode('UTF-8'), session_user.password):
        return True
    return False


def deserialize_labels(username: str):
    """
    :param username: to locate labels in file
    :return: label dict.
    """
    if not exists(username):
        return []
    with open(log, 'r') as users:
        _, username_line = exists(username)
        elements_line = username_line + 2
        return users.readlines()[elements_line]


def update_labels(session_user: User):
    """
    There is only one file representing the registry. We cannot change it line by line
    easily. To update the user registry we simply copy the file as a list of strings,
    edit the wanted label line, and then write everything back to the original file.
    :param session_user: that has updated labels. If not, nothing will happen.
    """
    if not exists(session_user.name):
        return
    users = open(log, 'r')
    lines = users.readlines()
    _, username_line = exists(session_user.name)
    users.close()

    with open(log, 'w') as users:
        elements_line = username_line + 2
        # To prevent multiple brackets being written inside other brackets on the file, we must remove them.
        new_elements = '{}'.format(session_user.elements).replace('{', '').replace('}', '')
        lines[elements_line] = 'elements: ' + '{' + new_elements + '}\n'
        users.writelines(lines)
