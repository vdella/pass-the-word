import os


class Constants:
    root_path = os.path.abspath('pass-the-word/resources')
    AUTH = root_path + '/auth.txt'
    DICT = root_path + '/dict.txt'

    @staticmethod
    def edit_given_path(artifact_path: str) -> str:
        """
        As Python works with relative paths when opening files,
        it will presume that we are calling a file that is inside
        the same directory as the caller of method open(file).

        We need to edit a given path string to be able to handle
        operations inside 'dict.txt'.
        """

        path = str(os.path.abspath(artifact_path))
        return path.replace('src/', '')
