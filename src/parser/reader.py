from src.path.path import Editor


class Reader:

    @staticmethod
    def words() -> dict and int:
        """
        Reads 'dict.txt' according to the returned path
        from Editor.edit_given_path() and puts every
        word inside a dict().

        :return: a dict[number] word and the max amount of words
        found inside 'dict.txt'
        """

        path = Editor().edit_given_path()
        file = open(path, 'r')
        lines = file.readlines()
        words = dict()
        iterator: int = 0

        for line in lines:
            words[iterator] = line
            iterator = iterator + 1
        return words, len(lines)
