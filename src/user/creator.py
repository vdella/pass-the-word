import bcrypt


class User:

    def __init__(self, username, password: str):
        self.name = username
        self.password = bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt())
        self.elements = dict()

    def create_label(self, name, element_to_be_stored: str):
        self.elements[name] = element_to_be_stored

    def show_elements(self):
        return self.elements
