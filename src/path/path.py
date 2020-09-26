import os


class Editor:

    @staticmethod
    def edit_given_path() -> str:
        path = str(os.path.abspath('resources/dict.txt'))
        return path.replace('src/password', '')
