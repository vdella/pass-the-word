from random import randint
from src.parser.wordreader import Reader


class Generator:

    @staticmethod
    def generate_password(split: bool) -> str:
        """
        :param split: Decides if the words will be separated by '-'.
        :return: 4 concatenated words from 'dict.txt'.
        """

        words, sup_limit = Reader.words()
        password = []

        for _ in range(4):
            word = words[randint(0, sup_limit)]
            word = word[:word.find('\n')]
            password.append(word)
        return '-'.join(password) if split else ''.join(password)
