from random import randint
from base64 import standard_b64encode
from src.parser.reader import Reader


class Generator:

    @staticmethod
    def gen_password_by_dict(split: bool) -> str:
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

    @staticmethod
    def gen_password_base64(phrase: str = None) -> bytes:
        """
        :param phrase: will be digested according to base64 alphabet.
        phrase can also be ''. In that case, we'll presume the user
        does not want to send a text for generating the password.
        :return: base64 digested string.
        """
        if phrase is None:
            return Generator.__gen_random()
        else:
            return standard_b64encode(phrase.encode('UTF-8'))

    @staticmethod
    def __gen_random() -> bytes:
        words = [randint(0, 255) for _ in range(18)]
        return standard_b64encode(bytes(words))
