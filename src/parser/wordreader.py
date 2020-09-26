from src.path import Editor


class Reader:

    @staticmethod
    def words() -> dict and int:
        path = Editor().edit_given_path()
        file = open(path, 'r')
        lines = file.readlines()
        words = dict()
        iterator: int = 0

        for line in lines:
            words[iterator] = line
            iterator = iterator + 1
        return words, len(lines)
