import os


class Editor:

    @staticmethod
    def edit_given_path() -> str:
        """
        As Python works with relative paths when opening files,
        it will presume that we are calling a file that is inside
        the same directory as the caller of method open(file).

        We need to edit a given path string to be able to handle
        operations inside 'dict.txt'.
        :return: 'dict.txt's path without string 'src/',
        which is added when we try to open() 'dict.txt' inside main.py.
        """

        path = str(os.path.abspath('resources/dict.txt'))
        return path.replace('src/', '')
