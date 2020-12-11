from random import randint
from base64 import standard_b64encode


class Generator:

    @staticmethod
    def __words() -> dict and int:
        """Reads 'dict.txt' and puts every
        word inside a dict().
        :return: a dict[number] word and the max amount of words (lines)
        found inside 'dict.txt'
        """
        file = open('../dict.txt', 'r')
        lines = file.readlines()
        words = dict()
        iterator: int = 0

        for line in lines:
            words[iterator] = line
            iterator = iterator + 1
        return words, len(lines)

    def gen_password_by_dict(self, split: bool) -> str:
        """:param split: Decides if the words will be separated by '-'.
        :return: 4 concatenated words from 'dict.txt'.
        """

        words, sup_limit = self.__words()
        password = []

        for _ in range(4):
            word = words[randint(0, sup_limit)]
            word = word[:word.find('\n')]
            password.append(word)
        return '-'.join(password) if split else ''.join(password)

    def gen_password_base64(self, seed: str = None) -> bytes:
        """:param seed: will be digested according to base64 alphabet.
        seed can also be ''. In that case, we'll presume the user
        does not want to send a text for generating the password.
        :return: base64 digested string.
        """
        if seed is None:
            return self.__gen_random()
        else:
            return standard_b64encode(seed.encode('UTF-8'))

    @staticmethod
    def __gen_random() -> bytes:
        words = [randint(0, 255) for _ in range(18)]
        return standard_b64encode(bytes(words))
